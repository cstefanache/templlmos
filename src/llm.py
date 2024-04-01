from llama_cpp import Llama
from huggingface_hub import hf_hub_download, scan_cache_dir


class LLM:
    def __init__(self, models):
        self.runtime_models = {}
        self.prompt_wrappers = {}
        self.default_wrappers = None

        for model in models:
            print(f"Downloading {model['repository']} from {model['model']}...")
            hf_hub_download(
                repo_id=model["repository"],
                filename=model["model"],
                cache_dir="./models",
            )
            if self.default_wrappers is None:
                self.default_wrappers = (
                    model["model"],
                    model["prefix"],
                    model["suffix"],
                    model["model"],
                    model["libraryPrefix"],
                    model["librarySuffix"],
                    model["depsPrefix"],
                    model.get("stop", None),
                )

            self.prompt_wrappers[model["model"]] = (
                model["model"],
                model["prefix"],
                model["suffix"],
                model["model"],
                model["libraryPrefix"],
                model["librarySuffix"],
                model["depsPrefix"],
                model.get("stop", None),
            )

            if model.get("library", False) is True:
                self.default_wrappers = (
                    self.default_wrappers[0],
                    self.default_wrappers[1],
                    self.default_wrappers[2],
                    model["model"],
                    model["libraryPrefix"],
                    model["librarySuffix"],
                    self.default_wrappers[5],
                    self.default_wrappers[6],
                )

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
                            n_gpu_layers=128,
                            n_threads=8,
                        )

    def get_prompt_wrappers(self, model_name=None):
        if model_name is not None:
            return self.prompt_wrappers[model_name]
        else:
            return self.default_wrappers

    def call_default_llm(self, instruction, dependencies="", update_fn=None):
        (name, pre, suff, lib_mode, lib_pre, lib_suff, deps_prefix, stop) = (
            self.default_wrappers
        )

        compiled_dependencies = (
            f"{deps_prefix} {dependencies}" if dependencies != "" else ""
        )
        dep_prefix = pre.replace("{deps}", compiled_dependencies)
        compiled_instruction = f"{dep_prefix} {instruction} {suff}"

        print("----------[ RealTime Compile ]----------")
        print(compiled_instruction)

        output = self.runtime_models[name](
            compiled_instruction,
            max_tokens=8096,
            top_k=40,
            seed=0,
            temperature=0.0,
            repeat_penalty=1.1,
            stream=True,
            stop=[stop],
        )

        # read from output stream generator
        result = ""
        for chunk in output:
            val = chunk["choices"][0]["text"]
            result += val
            if update_fn is not None:
                update_fn(val)
            print(val, end="")

        result += "\n```"
        if update_fn is not None:
            update_fn("\n```")
        return result

    def call_llm(
        self, model_name, instruction, include_stop=True, update_response=None
    ):
        model = self.runtime_models[model_name]
        (name, pre, suff, limb_model, lib_pre, lib_suff, deps_prefix, stop) = (
            self.prompt_wrappers[model_name]
        )
        output = model(
            instruction,
            max_tokens=4096,
            top_k=40,
            seed=0,
            temperature=0.0,
            repeat_penalty=1.1,
            stream=True,
            stop=[stop] if stop is not None and include_stop is True else None,
        )

        # read from output stream generator
        result = ""
        for chunk in output:
            val = chunk["choices"][0]["text"]
            if update_response is not None:
                update_response(val)
            result += val
            print(val, end="")

        result += "\n```"
        if update_response is not None:
            update_response("\n```")
        return result
