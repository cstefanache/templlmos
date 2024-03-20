import requests
import os
import json
import re
import json
from llama_cpp import Llama
from huggingface_hub import hf_hub_download, scan_cache_dir

CACHE = "./cache"
DEBUG = "./debug"


class Compiler:
    def __init__(self, filename, force_build=False):
        if not os.path.exists(CACHE):
            os.makedirs(CACHE)

        if not os.path.exists(DEBUG):
            os.makedirs(DEBUG)

        self.force_build = force_build
        self.filename = filename
        self.load_models()

    def load_models(self):
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)

            models = data["models"]

            for model in models:
                print(f"Downloading {model['repository']} from {model['model']}...")
                hf_hub_download(
                    repo_id=model["repository"],
                    filename=model["model"],
                    cache_dir="./models",
                )

            self.runtime_models = {}

            hf_cache_info = scan_cache_dir("./models")
            for repo in hf_cache_info.repos:
                print(f"Discovered repository: {repo.repo_id}")
                for revision in repo.revisions:
                    for file in revision.files:
                        if file.file_name.endswith(".gguf"):
                            print(f"Discovered model file: {file.file_name}")
                            self.runtime_models[file.file_name] = Llama(
                                str(file.file_path),
                                do_sample=True,
                                num_return_sequences=1,
                                n_ctx=4096,
                                n_gpu_layers=48,
                                n_threads=8,
                            )

    def run_compile(self):
        print("Compiling...")
        self.source_data = {}
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)
            html = self.compile(
                data["definition"], data["defaults"], filename=self.filename, html={}
            )

            for partial in data.get("partials", []):
                with open(f"./partials/{partial}", "r") as read_file:
                    partial_data = json.load(read_file)
                    self.compile(
                        partial_data["definition"],
                        data["defaults"],
                        filename=partial,
                        html=html,
                    )

            # stringify self.source_data
            self.source_data = json.dumps({"sources": self.source_data})
            self.source_data = self.source_data.replace("`", "\`")

            # html["head"]["script"]["_html_"].insert(
            #     0,
            #     {
            #         "id": "initial-storage",
            #         "result": f"```javascript\nconst sources = {self.source_data}\nif (localStorage.getItem('filesystem') === null) {{\n  localStorage.setItem('filesystem', JSON.stringify(sources))\n}}\n```",
            #     },
            # )
            json.dump(html, open("debug/output.json", "w"), indent=4)
            output = self.get_html_content("html", html)

            output_filename = re.sub(r"\.json", ".html", self.filename)
            with open(output_filename, "w") as file:
                file.write(output)

    def process_output(self, output):
        result = re.search(r"```[a-zA-Z ]+\n(.*?)```", output, re.DOTALL).group(1)

        return result

    def get_html_content(self, parent, value):
        output = f"\n"
        for key, value in value.items():
            if key == "_html_":
                output += "\n".join(
                    [
                        f"\n<{parent} id=\"{output['id']}\">\n{self.process_output(output['result'])}</{parent}>"
                        for output in value
                    ]
                )
            else:
                output += (
                    f"\n<{parent}>\n{self.get_html_content(key, value)}\n</{parent}>\n"
                )
        return output

    def call_llm(self, model_name, instruction):
        model = self.runtime_models[model_name]
        output = model(
            instruction,
            max_tokens=4096,
            top_k=10,
            temperature=0.0,
            repeat_penalty=1.1,
            stream=True,
            stop=["```\n"],
        )

        # read from output stream generator
        result = ""
        for chunk in output:
            val = chunk["choices"][0]["text"]
            result += val
            print(val, end="")

        result += "\n```"
        return result

        # result = output["choices"][0]["text"]
        # print("#######################")
        # print(result)
        # return result

    def generate(self, definition, parent, current_defs, partial=""):
        id = definition.get("id", "undefined")
        disabled = definition.get("disabled", False)
        rebuild = definition.get("rebuild", False)

        if "_defaults" in definition.keys():
            for def_key, def_value in definition["_defaults"].items():
                current_defs[def_key] = def_value

        if disabled:
            print(f"Skipping {id} for {parent} because it is disabled")
            return None

        instruction = definition.get("instruction", None)
        instructions = definition.get("instructions", [])

        suffix = current_defs.get("suffix", "")
        prefix = current_defs.get("prefix", "")
        model = current_defs.get("model", None)

        if len(instructions) > 0:
            instruction = "\n".join(instructions)

        cache = f"{CACHE}/{id}.json"
        compiled_instruction = f"{prefix} {instruction} {suffix}"

        partial = re.sub(r"\.json", "", partial)
        if partial not in self.source_data.keys():
            self.source_data[partial] = {}

        # check if last element in string pattern "a > b > c" is "script"
        source_name = id
        if parent.split(" > ")[-1] == "script":
            source_name += ".script"
        elif parent.split(" > ")[-1] == "style":
            source_name += ".style"

        if os.path.exists(cache):
            with open(cache, "r") as file:
                result = json.load(file)

                if (
                    rebuild is False
                    and self.force_build is False
                    and result["compiled_instruction"] == compiled_instruction
                ):
                    print(f"Using cache for {id}")

                    self.source_data[partial][source_name] = (
                        "\n----------------[ prompt ]----------------\n"
                        + compiled_instruction
                        + "\n----------------[ output ]----------------\n"
                        + result["output"]
                    )

                    return result["output"]
                else:
                    print(f"Cache for {id} is outdated, recompiling...")

        print(f"Compiling {id}...")

        result = self.call_llm(model, compiled_instruction)

        self.source_data[partial][source_name] = (
            "\n----------------[ prompt ]----------------\n"
            + compiled_instruction
            + "\n----------------[ output ]----------------\n"
            + result
        )

        with open(cache, "w") as file:
            file.write(
                json.dumps(
                    {"compiled_instruction": compiled_instruction, "output": result}
                )
            )

        with open(f"{DEBUG}/{id}.md", "w") as file:
            file.write(
                f"## {id}\n\n### Instruction\n```\n{compiled_instruction}\n```\n\n```\n{self.process_output(result)}\n```"
            )

        return result

    def go_into_tag(
        self, definition, current_element, current_defs, parent, partial=""
    ):
        print(f"Generating for {parent}...")

        if isinstance(definition, list):
            for item in definition:
                self.go_into_tag(
                    item, current_element, current_defs, parent, partial=partial
                )
            return

        if "_defaults" in definition.keys():
            for def_key, def_value in definition["_defaults"].items():
                current_defs[def_key] = def_value

        if "_generate" in definition.keys():
            current_element["_html_"] = current_element.get("_html_", [])

            if isinstance(definition["_generate"], list):
                for item in definition["_generate"]:
                    result = self.generate(item, parent, current_defs, partial=partial)
                    if result is not None:
                        current_element["_html_"].append(
                            {"id": item["id"], "result": result}
                        )
            else:
                result = self.generate(definition["_generate"], parent, current_defs)
                if result is not None:
                    current_element["_html_"].append(
                        {"id": item["id"], "result": result}
                    )

        for key, value in definition.items():
            if key not in ["_defaults", "_generate"]:
                if key not in current_element.keys():
                    current_element[key] = {"_html_": []}
                self.go_into_tag(
                    value,
                    current_element[key],
                    current_defs,
                    parent + " > " + key,
                    partial=partial,
                )

    def compile(self, data, defaults, filename, html={}):
        for key, value in data.items():
            parent = "html"
            if key not in html.keys():
                html[key] = {}

            current_defs = {}
            for def_key, def_value in defaults.items():
                current_defs[def_key] = def_value

            parent += " > " + key
            self.go_into_tag(value, html[key], current_defs, parent, filename)

        return html


if __name__ == "__main__":
    Compiler("templlmos.json", force_build=False).run_compile()
