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
        self.api = {}

    def process_output(self, output, single_group=True):
        print("#"*80)
        print(output)
        print("#"*80)
        if single_group:
            result = re.search(r"```[a-z]+\n(.*?)```",
                               output, re.DOTALL).group(1)
            return result
        else:
            groups = re.findall(r"```[a-z]+\n(.*?)```", output, re.DOTALL)
            result = ""
            for group in groups:
                result += group + "\n"
            return result

    def get_api(self, output_src):
        local_api = ""
        for line in output_src.split("\n"):
            if re.search(r" ?\/?\*", line):
                local_api += line + "\n"
            elif re.search(r"[a-zA-Z.]+ = function", line) or re.search(
                r"^function [a-z]", line
            ):
                local_api += line.strip() + " ... }\n"
        return local_api

    def compile(self, partial, html, api, update_response=None):
        for app, packages in partial.items():
            for package_id, package in packages.items():
                dependencies = package.get("dependencies", [])
                rebuild = package.get("rebuild", False)
                preventRebuild = package.get("preventRebuild", False)
                library = package.get("library", False)
                to = package.get("to")
                tag = package.get("tag")
                max_tokens = package.get("max_tokens", 2048)
                instructions = package.get("instructions")

                compiled_dependencies = ""

                if package.get("disabled", False):
                    print(f"Skipping disabled package: {package_id}")
                    continue

                for dependency in dependencies:
                    try:
                        compiled_dependencies += api[dependency] + "\n"
                    except KeyError:
                        print(f"Dependency not found: {dependency}")
                to = to.split(".")
                to_html = html
                for path in to:
                    if path not in to_html.keys():
                        to_html[path] = {"_children_": []}
                    to_html = to_html[path]
                package_src = ""
                package_api = ""
                for index, instruction_set in enumerate(instructions):
                    local_api = ""
                    instruction = "\n".join(instruction_set)

                    compiled_instruction = self.llm.get_instruction(
                        instruction, compiled_dependencies, to, tag, library
                    )

                    cache_file_name = f"{CACHE}/{app}_{package_id}_{index}.json"
                    skip_compilation = False

                    crc = binascii.crc32(compiled_instruction.encode())
                    if (
                        not rebuild
                        and not self.recompile
                        and os.path.exists(cache_file_name)
                    ):
                        with open(cache_file_name, "r") as file:
                            cache_data = json.load(file)
                            if cache_data["crc"] == crc or preventRebuild:
                                print(
                                    f"Using cache for {app}_{package_id}_{index}...")
                                skip_compilation = True
                                output_src = cache_data["output"]
                                package_src += cache_data["output"]

                    if not skip_compilation:
                        print(
                            f"----------[ {app} {package_id} {index} {max_tokens}]----------")
                        print(compiled_instruction)
                        result = self.llm.execute(
                            instruction, compiled_dependencies, to, tag, library, max_tokens=max_tokens
                        )
                        output_src = self.process_output(result)
                        package_src += output_src
                        cache_data = {
                            "crc": crc,
                            "compiled_instruction": compiled_instruction,
                            "result": result,
                            "output": output_src,
                        }

                    if tag == "script":
                        local_api += self.get_api(output_src)

                        compiled_dependencies += local_api
                    cache_data["library"] = local_api

                    if not skip_compilation:
                        with open(cache_file_name, "w") as file:
                            json.dump(cache_data, file, indent=4)

                    # write debug markdown file
                    with open(f"{DEBUG}/{app}_{package_id}_{index}.md", "w") as file:
                        file.write(f"## {app}_{package_id}_{index}\n")
                        file.write("### API\n\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>\n{local_api}\n</pre>\n")

                        file.write("### Instruction\n\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>\n{instruction}\n</pre>\n"
                        )
                        file.write("### Output\n\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>\n{package_src}\n</pre>\n"
                        )

                    package_api += local_api

                api[package_id] = package_api

                html_output = f"<{tag} id='{app}_{package_id}'>\n"
                if tag == "script":
                    html_output += "(() => {\n"

                if tag == "script":
                    html_output += package_src + "\n})()\n"
                else:
                    html_output += package_src

                html_output += f"</{tag}>"

                to_html["_children_"].append(html_output)

    def _compile(self, partial, html, api, update_response=None):
        (
            model,
            model_prefix,
            model_suffix,
            library_model,
            library_prefix,
            library_suffix,
            deps_prefix,
            stop,
        ) = self.llm.get_prompt_wrappers()
        for app, packages in partial.items():
            app_model = packages.get("model", model)
            app_prefix = packages.get("prefix", model_prefix)
            app_suffix = packages.get("suffix", model_suffix)
            app_deps_prefix = packages.get("depsPrefix", deps_prefix)
            app_library_prefix = packages.get("libraryPrefix", library_prefix)
            app_library_suffix = packages.get("librarySuffix", library_suffix)
            for package_id, package in packages.items():
                prefix = package.get("prefix", app_prefix)
                suffix = package.get("suffix", app_suffix)
                package_library_prefix = package.get(
                    "libraryPrefix", app_library_prefix
                )
                package_library_suffix = package.get(
                    "librarySuffix", app_library_suffix
                )
                package_deps_prefix = package.get(
                    "depsPrefix", app_deps_prefix)
                model = package.get("model", app_model)
                dependencies = package.get("dependencies", [])
                disabled = package.get("disabled", False)
                rebuild = package.get("rebuild", False)
                preventRebuild = package.get("preventRebuild", False)
                library = package.get("library", False)

                compiled_dependencies = ""
                for dependency in dependencies:
                    try:
                        compiled_dependencies += api[dependency] + "\n"
                    except KeyError:
                        print(f"Dependency not found: {dependency}")

                compiled_dependencies = f"{package_deps_prefix} {compiled_dependencies}"

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

                package_src = ""
                package_api = ""
                for index, instruction_set in enumerate(instructions):
                    local_api = ""
                    instruction = "\n".join(instruction_set)
                    dep_prefix = prefix.replace(
                        "{deps}", compiled_dependencies)
                    compiled_instruction = f"{dep_prefix} {instruction} {suffix}"

                    cache_file_name = f"{CACHE}/{app}_{package_id}_{index}.json"
                    skip_compilation = False

                    crc = binascii.crc32(compiled_instruction.encode())
                    if (
                        not rebuild
                        and not self.recompile
                        and os.path.exists(cache_file_name)
                    ):
                        with open(cache_file_name, "r") as file:
                            cache_data = json.load(file)
                            if cache_data["crc"] == crc or preventRebuild:
                                print(
                                    f"Using cache for {app}_{package_id}_{index}...")
                                skip_compilation = True
                                output_src = cache_data["output"]
                                package_src += cache_data["output"]

                    if not skip_compilation:
                        # print(
                        # f"----------[ {app} {package_id} {index} ]----------")
                        # print(compiled_instruction)
                        result = self.llm.call_llm(
                            model, compiled_instruction, update_response=update_response
                        )
                        output_src = self.process_output(result)
                        package_src += output_src
                        cache_data = {
                            "crc": crc,
                            "compiled_instruction": compiled_instruction,
                            "output": output_src,
                        }

                    if tag == "script":
                        local_api += self.get_api(output_src)

                        compiled_dependencies += local_api
                    cache_data["library"] = local_api

                    if not skip_compilation:
                        with open(cache_file_name, "w") as file:
                            json.dump(cache_data, file, indent=4)

                    # write debug markdown file
                    with open(f"{DEBUG}/{app}_{package_id}_{index}.md", "w") as file:
                        file.write(f"## {app}_{package_id}_{index}\n")
                        file.write("### API\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>{local_api}</pre>\n")

                        file.write("### Instruction\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>{instruction}</pre>\n"
                        )
                        file.write("### Output\n")
                        file.write(
                            f"<pre style='text-wrap: wrap'>{package_src}</pre>\n"
                        )

                    package_api += local_api

                api[package_id] = package_api

                html_output = f"<{tag} id='{app}_{package_id}'>\n"
                if tag == "script":
                    html_output += "(() => {\n"

                if tag == "script":
                    html_output += package_src + "\n})()\n"
                else:
                    html_output += package_src

                html_output += f"</{tag}>"

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

    def build(self, update_response=None):
        # print("Compiling...")

        html = {
            "head": {"_children_": []},
            "body": {"_children_": []},
            "_children_": [],
        }
        sources = []
        for partial in self.data.get("partials", []):
            with open(f"./partials/{partial}", "r") as read_file:
                partial_data = json.load(read_file)

                for app, packages in partial_data.items():
                    for package_id, package in packages.items():
                        # print("*"*100)
                        # print(
                        # f"Compiling package: {app} {package_id} {package}...")

                        for index, _ in enumerate(package.get("instructions", [])):
                            debug_file_name = f"{DEBUG}/{app}_{package_id}_{index}.md"

                            try:
                                with open(debug_file_name, "r") as file:
                                    source = file.read()
                                    source = source.replace(
                                        "'", '"').replace("\n", "\\n")

                                    name = partial[:-5].replace("chatgpt_", "")
                                    sources.append(
                                        f"window.os.fs.write('/sources/{name}/{package_id}_{index}.md', '{source}')"
                                    )
                            except FileNotFoundError:
                                print(">>>>"+debug_file_name)
                                pass

                self.compile(
                    partial_data, html, self.api, update_response=update_response
                )

        gen = "\n".join(sources)
        html["body"]["_children_"].append(f"<script>{gen}</script>")

        # read presentation.md file
        for file_name in ["presentation", "conclusions"]:
            with open(f"./{file_name}.md", "r") as file:
                presentation = file.read()

                presentation = presentation.replace(
                    "'", '"').replace("\n", "\\n")

                html["body"]["_children_"].append(
                    f"<script>window.os.fs.write('/{file_name}.xmd', '{presentation}')</script>")

        with open(f"{DEBUG}/compiled.json", "w") as file:
            json.dump(html, file, indent=4)

        root = "<html>" + self.get_html(html) + "</html>"
        soup = bs(root, "html.parser")

        return soup.prettify()
