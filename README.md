# TempLLM OS

Inspired by Andrej Karpathy's: "The hottest new programming language is English" and [this tweet](https://twitter.com/karpathy/status/1707437820045062561?lang=en) I've created `TempLLMOS` (webOS) entirely coded in natural language and seamlessly compiled into JavaScript using an advanced Large Language Model.

![Image](assets/templlmos.gif)

To test it just open the `templllmos.html` file in a browser or [test it online](https://cstefanache.github.io/templlmos/templlmos.html)

### What's implemented so far:
- a pseudo-filesystem developed on top of localStorage - hey - it works!
- a GUI with windows, toolbars and statusbars
- three applications: `file browser`, `minesweeper` and `text editor` (more to come - feel free to contribute)

### Why Natural Language WebOS?

- **Ease of Use:** Make coding accessible and intuitive for everyone, regardless of their programming background.
- **Innovative Approach:** Leveraging the latest advancements in AI and natural language processing.

## Next Steps

- [ ] Runtime Compiler
- [ ] Better Low-Level APIs
- [ ] Improved FS
- [ ] IDE

## Structure

`compiler.py` - the compiler that transforms the text into code
`templlmos.json` - the root file for the source codes. mostly import partials
`partials` - the folder that contains all the natural language source code.
`cache` - is just a folder of cached responses to avoid rebuilding the entire os on change. Don't worry it is compiling only deltas or you can enforce with `"rebuild": true` in the source definition
`debug` - just debugging output (source code is available published in the OS itself under `sources` folder)


## Try it out

Install dependencies:

```
python3 -m pip install huggingface_hub llama-cpp-python watchdog
```

Ona a mac (Metal)

`CMAKE_ARGS="-DLLAMA_METAL=on" python3 -m pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir`


Run compiler:

```
python3 compiler.py
```


## Contibute

Contributions are welcome