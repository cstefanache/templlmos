import requests
import os
import json
import re
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

    def process_output(self, output):
        result = re.search(r"```[a-zA-Z ]+\n(.*?)```", output, re.DOTALL).group(1)
        return result

    def get_html_content(self, parent, value):
        print(f"Generating HTML for {parent}...")
        print(json.dumps(value, indent=4))
        output = f"\n"
        for key, content in value.items():
            if key == "_id_":
                continue

            if key == "_html_":
                output += "\n".join(
                    [
                        f"\n<{parent} id=\"{value['_id_']}\"></{parent}>"
                        for chunk in content
                    ]
                )
            else:
                output += f"\n<{parent}>\n{self.get_html_content(key, content)}\n</{parent}>\n"
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

    def generate(self, definition, parent, current_defs, partial=""):
        pass

    def go_into_tag(
        self, definition, current_element, current_defs, parent, partial=""
    ):
        print(f"Generating for {parent}...")
        pass

    def get_default(self, root, current_defaults):
        if "_defaults" in root.keys():
            for def_key, def_value in root["_defaults"].items():
                current_defaults[def_key] = def_value

        return current_defaults

    def compile(self, data, defaults, filename, html):

        for id, value in data.items():
            elements = value.get("elements", [])
            current_defaults = self.get_default(value.get("defaults", {}), defaults)
            for element in elements:
                tag = element.get("tag", None)
                disabled = element.get("disabled", False)
                rebuild = element.get("rebuild", False)

                if disabled is True:
                    continue

                instruction_defaults = self.get_default(
                    element, self.clone_defaults(current_defaults)
                )
                to = element.get("to", [])
                to = to.split(".") + [tag]
                to_html = html
                for path in to:
                    if path not in to_html.keys():
                        to_html[path] = {}
                    to_html = to_html[path]

                instructions = element.get("instructions", None)
                skip_compilation = True
                compiled_instructions = []
                for instruction_set in instructions:
                    output = to_html.get("_html_", [])
                    suffix = instruction_defaults.get("suffix", "")
                    prefix = instruction_defaults.get("prefix", "")
                    model = instruction_defaults.get("model", None)
                    result = None
                    instruction = "\n".join(instruction_set)
                    cache = f"{CACHE}/{id}.json"
                    compiled_instruction = f"{prefix} {instruction} {suffix}"
                    compiled_instructions.append(compiled_instruction)
                    if os.path.exists(cache):
                        with open(cache, "r") as file:
                            cache_data = json.load(file)
                          
                            if (
                                rebuild is False
                                and self.force_build is False
                                and cache_data["compiled_instruction"]
                                == compiled_instruction
                            ):
                                print(f"Using cache for {id}")
                                skip_compilation = True
                                output.append(cache_data["output"])
                            else:
                                print(f"Cache for {id} is outdated, recompiling...")

                if skip_compilation is False:
                    print(f"Compiling... {id}")
                    result = self.call_llm(model, compiled_instruction)
                    with open(cache, "w") as file:
                        file.write(
                            json.dumps(
                                {
                                    "compiled_instruction": compiled_instruction,
                                    "output": result,
                                },
                                indent=4,
                            )
                        )

                    to_html["_id_"] = f"{tag}-{id}"
                    to_html["_html_"] = output

        return html

    def clone_defaults(self, defaults):
        return {k: v for k, v in defaults.items()}

    def run_compile(self):
        print("Compiling...")
        html = {}
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)
            defaults = data["defaults"]
            current_defs = self.clone_defaults(defaults)
            self.compile(
                data["definition"], current_defs, filename=self.filename, html=html
            )

            for partial in data.get("partials", []):
                print(f"Compiling partial: {partial}...")
                with open(f"./partials/{partial}", "r") as read_file:
                    partial_data = json.load(read_file)
                    current_defs = self.clone_defaults(defaults)
                    self.compile(
                        partial_data,
                        current_defs,
                        filename=partial,
                        html=html,
                    )

        json_output = json.dumps(html, indent=4)
        #write json_output to file
        with open("a.json", "w") as file:
            file.write(json_output)
        
        # output = self.get_html_content("html", html)
        # output_filename = re.sub(r"\.json", ".html", self.filename)
        # with open(output_filename, "w") as file:
        #     file.write(output)


if __name__ == "__main__":
    Compiler("templlmos.json", force_build=True).run_compile()
