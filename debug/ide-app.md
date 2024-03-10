## ide-app

### Instruction
```
Generate JS code using `let` instead of `var`. All the `os` functions are already defined.
### Instruction:
 Create an async self executing function that defines a function called `ide` on the `window.os.apps` object that takes a parameter `path` and having the following functionality:
* creates a root dom element with the class `editor`
* call `os.gui.createWindow` with the following parameters: `'📄 IDE' {path || ''}`, created root DOM element, `700`, `600` and store the returned value to constant `win`
* call `os.gui.toolbar(win)` and store the returned value to constant `toolbar`
* add a `textarea` element with id `code` to the root dom element, 100% width and 400px height and nowrap for white-space
* add a readonly `textarea` element with id `result` to the root dom element, 100% width and 130px height and nowrap for white-space
* if the path is not empty, store result of executiing `os.fs.readPath` into `content` constant and set it to the `textarea`
* create an internal function `save` that:
 - if the path is not empty, store the value of the `textarea` to the `content` constant and call `os.fs.write` with the `path` and `textarea` value
 - if the path is empty, call `os.gui.createPrompt` with the following parameters: `'Save File'` and `os.gui.createPrompt('Enter folder name', path => os.fs.write(path, textarea.value))`
* create an internal function `run` that:
 - replace the `result` textarea value with the result `Compiling...`
 - await for call `os.runtime.compile` with the `textarea` value
 - replace the `result` textarea value with the result of the `os.runtime.compile`
* call `toolbar.addButton` with parameters '💾' and `() => save()`
* call `toolbar.addButton` with parameters '▶️' and `() => run()` 
### Response:

```

```
(async () => {
  window.os.apps.ide = async (path) => {
    const root = document.createElement('div');
    root.className = 'editor';
    document.body.appendChild(root);
    
    const win = os.gui.createWindow('📄 IDE', root, 700, 600);
    const toolbar = os.gui.toolbar(win);
    
    const textarea = document.createElement('textarea');
    textarea.id = 'code';
    textarea.style.width = '100%';
    textarea.style.height = '400px';
    textarea.style.whiteSpace = 'nowrap';
    root.appendChild(textarea);
    
    const result = document.createElement('textarea');
    result.id = 'result';
    result.style.width = '100%';
    result.style.height = '130px';
    result.style.whiteSpace = 'nowrap';
    result.readOnly = true;
    root.appendChild(result);
    
    if (path) {
      const content = await os.fs.readPath(path);
      textarea.value = content;
    }
    
    const save = () => {
      if (path) {
        const content = textarea.value;
        os.fs.write(path, content);
      } else {
        os.gui.createPrompt('Save File', (newPath) => {
          os.fs.write(newPath, textarea.value);
        });
      }
    };
    
    const run = async () => {
      result.value = 'Compiling...';
      const compiled = await os.runtime.compile(textarea.value);
      result.value = compiled;
    };
    
    toolbar.addButton('💾', () => save());
    toolbar.addButton('▶️', () => run());
  };
})();


```