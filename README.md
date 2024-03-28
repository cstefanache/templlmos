# TempLLM OS

`TempLLMOS` (webOS) entirely coded in natural language and seamlessly compiled into JavaScript using an LLM.


![Image](assets/templlmos.gif)

This project was inspired by Andrej Karpathy's: "The hottest new programming language is English" and [this tweet](https://twitter.com/karpathy/status/1707437820045062561?lang=en)


### Sample
Here is how to code a simple text viewer
```
Create a self executing function that defines a function called `viewer` on the `window.os.apps` object having the following functionality:,
 - The `viewer` function accepts one parameter `path` and have the following functionality:
 - creates a new `div` element with the class `viewer`", 
 - call `os.gui.createWindow` with the following parameters: `View: `+ path, created DOM element
 - call `os.fs.readPath` with the parameter `path` and store it in a variable `content`
 - create a new `pre` element with the class `content` and set its innerHTML to `content`
 - append the `pre` element to the created DOM element
```

# Give it a try:

There are two working modes for the experimental os: Static runtime where the precompiled code is present and injected in the root HTML and the dynamic realtime compiler mode where a server that hosts a LLM model is published that allows the user to compile new apps at runtime.

- [Static Runtime on GitHub pages](https://cstefanache.github.io/templlmos/templlmos.html)
- Static Runtime: Just open the `templllmos.html` file
- Realtime Compiler: `python3 templlmos.py --serve --listen` and open `http://localhost:8080` in a browser 

For runtime compiler you need to install dependencies:

```
python3 -m pip install huggingface_hub llama-cpp-python watchdog
```

for MAC runtime you can benefit from GPU inference and install llama-cpp with METAL enabled:

```
CMAKE_ARGS="-DLLAMA_METAL=on" python3 -m pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```


### What's implemented so far:
- a pseudo-filesystem developed on top of localStorage - hey - it works!
- a GUI with windows, toolbars and statusbars
- three applications: `file browser`, `minesweeper` and `text editor` (more to come - feel free to contribute)

### Why Natural Language WebOS?

- **Ease of Use:** Make coding accessible and intuitive for everyone, regardless of their programming background.
- **Innovative Approach:** Leveraging the latest advancements in AI and natural language processing.

## Next Steps

- [x] Runtime Compiler
- [x] IDE
- [x] Restructure code descriptors
- [x] Better Low-Level APIs
- [ ] Improved FS
- [x] Remove dependency of API code calls `os.gui.createWindow` by injecting low-level APIs into context


## Structure

`compiler.py` - the compiler that transforms the text into code
`templlmos.json` - the root file for the source codes. mostly import partials
`partials` - the folder that contains all the natural language source code.
`cache` - is just a folder of cached responses to avoid rebuilding the entire os on change. Don't worry it is compiling only deltas or you can enforce with `"rebuild": true` in the source definition
`debug` - just debugging output (source code is available published in the OS itself under `sources` folder)


## Contibute

Contributions are welcome: ideas, compiler code, applications