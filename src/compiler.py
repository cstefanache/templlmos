import os
import re
import json
import binascii
from bs4 import BeautifulSoup as bs

CACHE = "./cache"
DEBUG = "./debug"


class Compiler:
    def __init__(self, llm, data, recompile=False):
        if not os.path.exists(CACHE):
            os.makedirs(CACHE)

        if not os.path.exists(DEBUG):
            os.makedirs(DEBUG)

        self.recompile = recompile
        self.llm = llm
        self.data = data

    def process_output(self, output):
        result = re.search(r"```[a-zA-Z ]+\n(.*?)```", output, re.DOTALL).group(1)
        return result

    def compile(self, partial, html, api):
        (model, model_prefix, model_suffix, stop) = self.llm.get_prompt_wrappers()
        for app, packages in partial.items():
            app_model = packages.get("model", model)
            app_prefix = packages.get("prefix", model_prefix)
            app_suffix = packages.get("suffix", model_suffix)
            self_api = ""
            for package_id, package in packages.items():
                prefix = package.get("prefix", app_prefix)
                suffix = package.get("suffix", app_suffix)
                model = package.get("model", app_model)
                dependencies = package.get("dependencies", [])
                disabled = package.get("disabled", False)
                rebuild = package.get("rebuild", False)
                library = package.get("library", False)

                compiled_dependencies = ""
                for dependency in dependencies:
                    compiled_dependencies += api[dependency]

                print(
                    f"Processing package: {package_id}. Rebuild: {rebuild}, disabled: {disabled}"
                )

                to = package.get("to")
                tag = package.get("tag")
                instructions = package.get("instructions")

                if disabled:
                    print(f"Skipping disabled package: {package_id}")
                    continue

                to = to.split(".")
                to_html = html
                for path in to:
                    if path not in to_html.keys():
                        to_html[path] = {"_children_": []}
                    to_html = to_html[path]

                compiled_instructions = []
                for instruction_set in instructions:
                    instruction = "\n".join(instruction_set)
                    dep_prefix = prefix.replace("{deps}", compiled_dependencies)
                    compiled_instruction = f"{dep_prefix} {instruction} {suffix}"
                    compiled_instructions.append(compiled_instruction)

                cache_file_name = f"{CACHE}/{app}_{package_id}.json"
                skip_compilation = False
                instructions_set = "\n".join(
                    ["\n".join(instruction) for instruction in compiled_instructions]
                )
                crc = binascii.crc32(instructions_set.encode())

                if (
                    not rebuild
                    and not self.recompile
                    and os.path.exists(cache_file_name)
                ):
                    with open(cache_file_name, "r") as file:
                        cache_data = json.load(file)
                        if cache_data["crc"] == crc:
                            print(f"Using cache for {app}_{package_id}")
                            skip_compilation = True
                            output = cache_data["output"]

                if not skip_compilation:
                    print(f"Compiling {app} - {package_id} ...")

                    output = []
                    for instruction in compiled_instructions:
                        result = self.llm.call_llm(model, instruction)
                        output.append(result)

                    cache_data = {
                        "crc": crc,
                        "compiled_instruction": compiled_instructions,
                        "output": output,
                    }

                html_output = f"<{tag} id='{app}_{package_id}'>\n"
                if tag == "script":
                    html_output += "(() => {\n"

                package_src = ""
                for res in output:
                    package_src += self.process_output(res)

                if library:
                    if not skip_compilation or "library" not in cache_data:
                        libraryPrefix = package.get("libraryPrefix", prefix)
                        librarySuffix = package.get("librarySuffix", suffix)
                        self_api = self.llm.call_llm(
                            model, f"{libraryPrefix} {package_src} {librarySuffix}"
                        )
                        cache_data["library"] = self_api
                    else:
                        self_api = cache_data["library"]
                        print('>>> setting self_api from cache', package_id)

                    api[package_id] = self_api

                if tag == "script":
                    html_output += package_src + "\n})()\n"
                else:
                    html_output += package_src

                html_output += f"</{tag}>"

                if not skip_compilation:
                    with open(cache_file_name, "w") as file:
                        json.dump(cache_data, file, indent=4)

                to_html["_children_"].append(html_output)

    def get_html(self, html):
        result = ""
        for tag, value in html.items():
            if tag == "_children_":
                for child in value:
                    result += child
            else:
                result += f"<{tag}>{self.get_html(value)}</{tag}>"
        return result

    def build(self):
        print("Compiling...")
        api = {}
        html = {
            "head": {"_children_": []},
            "body": {"_children_": []},
            "_children_": [],
        }
        for partial in self.data.get("partials", []):
            print(f"Compiling partial: {partial}...")
            with open(f"./partials/{partial}", "r") as read_file:
                partial_data = json.load(read_file)
                self.compile(partial_data, html, api)

        with open(f"{DEBUG}/compiled.json", "w") as file:
            json.dump(html, file, indent=4)

        root = "<html>" + self.get_html(html) + "</html>"
        soup = bs(root, "html.parser")

        return soup.prettify()
