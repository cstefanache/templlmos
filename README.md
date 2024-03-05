# templlmos

Install dependencies:

```
python3 -m pip install huggingface_hub
python3 -m pip install llama-cpp-python
```


## Mac (Metal)

`CMAKE_ARGS="-DLLAMA_METAL=on" python3 -m pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir`