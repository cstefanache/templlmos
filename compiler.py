import requests
import os
import json
import re
import json
from llama_cpp import Llama
from huggingface_hub import hf_hub_download, scan_cache_dir

CACHE = "./cache"


class Compiler:
    def __init__(self, filename, force_build=False):
        if not os.path.exists(CACHE):
            os.makedirs(CACHE)

        self.force_build = force_build

        with open(filename, "r") as read_file:
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

            self.compile(data["definition"], data["defaults"], filename=filename)

    def evaluate_ruleset(self, ruleset, output):
        return "tbd"

    def call_llm(self, model_name, instruction):
        model = self.runtime_models[model_name]
        output = model(
            instruction,
            max_tokens=1024,
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

        result += "\n```"
        return result

        # result = output["choices"][0]["text"]
        # print("#######################")
        # print(result)
        # return result

    def generate(self, definition, parent, current_defs):
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

        if os.path.exists(cache):
            with open(cache, "r") as file:
                result = json.load(file)

                if (
                    rebuild is False
                    and self.force_build is False
                    and result["compiled_instruction"] == compiled_instruction
                ):
                    print(f"Using cache for {id}")
                    return result["output"]
                else:
                    print(f"Cache for {id} is outdated, recompiling...")

        print(f"Compiling {id}...")

        result = self.call_llm(model, compiled_instruction)

        with open(cache, "w") as file:
            file.write(
                json.dumps(
                    {"compiled_instruction": compiled_instruction, "output": result}
                )
            )

        return result

    def go_into_tag(self, definition, current_element, current_defs, parent):
        print(f"Generating for {parent}...")

        if isinstance(definition, list):
            for item in definition:
                self.go_into_tag(item, current_element, current_defs, parent)
            return

        if "_defaults" in definition.keys():
            for def_key, def_value in definition["_defaults"].items():
                current_defs[def_key] = def_value

        if "_generate" in definition.keys():
            current_element["_html_"] = current_element.get("_html_", [])

            if isinstance(definition["_generate"], list):
                for item in definition["_generate"]:
                    result = self.generate(item, parent, current_defs)
                    if result is not None:
                        current_element["_html_"].append(result)
            else:
                result = self.generate(definition["_generate"], parent, current_defs)
                if result is not None:
                    current_element["_html_"].append(result)

        for key, value in definition.items():
            if key not in ["_defaults", "_generate"]:
                if key not in current_element.keys():
                    current_element[key] = {"_html_": []}
                self.go_into_tag(
                    value, current_element[key], current_defs, parent + " > " + key
                )

    def compile(self, data, defaults, filename):
        print("----------------------------")
        html = {}

        for key, value in data.items():
            parent = "html"
            if key not in html.keys():
                html[key] = {}

            current_defs = {}
            for def_key, def_value in defaults.items():
                current_defs[def_key] = def_value

            parent += " > " + key
            self.go_into_tag(value, html[key], current_defs, parent)

        print(json.dumps(html, indent=4))

        def process_output(output):
            print("\n\n")
            print(output)
            result = re.search(r"```[a-zA-Z ]+\n(.*?)```", output, re.DOTALL).group(1)

            return result

        def get_html_content(parent, value):
            output = f"\n<{parent}>"
            for key, value in value.items():
                if key == "_html_":
                    output += "\n".join(
                        [f"\n{process_output(output)}" for output in value]
                    )
                else:
                    output += get_html_content(key, value)
            return output + f"\n</{parent}>"

        output = get_html_content("html", html)

        output_filename = re.sub(r"\.json", ".html", filename)
        with open(output_filename, "w") as file:
            file.write(output)


Compiler("templlmos.json", force_build=False)
