## editor-app

### Instruction
```
Generate JS code using `let` instead of `var`. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that defines a function called `editor` on the `window.os.apps` object that takes a parameter `path` and having the following functionality:
* creates a root dom element with the class `editor`
* call `os.gui.createWindow` with the following parameters: `'📄 Text Editor' {path || ''}`, created root DOM element, `700`, `500` and store the returned value to constant `win`
* call `os.gui.toolbar(win)` and store the returned value to constant `toolbar`
* call `toolbar.addButton` with parameters '💾' and `() => save()`
* add a `textarea` element to the root dom element, 100% width and height and nowrap for white-space
* if the path is not empty, store result of executiing `os.fs.readPath` into `content` constant and set it to the `textarea`
* create an internal function `save` that:
 - if the path is not empty, store the value of the `textarea` to the `content` constant and call `os.fs.write` with the `path` and `textarea` value
 - if the path is empty, call `os.gui.createPrompt` with the following parameters: `'Save File'` and `os.gui.createPrompt('Enter folder name', path => os.fs.write(path, textarea.value))` 
### Response:

```

```
(function() {
    window.os.apps.editor = function(path) {
        const root = document.createElement('div');
        root.className = 'editor';
        document.body.appendChild(root);
        
        const win = os.gui.createWindow('📄 Text Editor', root, 700, 500);
        const toolbar = os.gui.toolbar(win);
        toolbar.addButton('💾', save);
        
        const textarea = document.createElement('textarea');
        textarea.style.width = '100%';
        textarea.style.height = '100%';
        textarea.style.whiteSpace = 'nowrap';
        root.appendChild(textarea);
        
        let content = '';
        if (path) {
            content = os.fs.readPath(path);
            textarea.value = content;
        }
        
        function save() {
            if (path) {
                content = textarea.value;
                os.fs.write(path, content);
            } else {
                os.gui.createPrompt('Save File', (newPath) => {
                    os.fs.write(newPath, textarea.value);
                });
            }
        }
    };
})();


```