## browser-app

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined on global scope.
### Instruction:
 Create a self executing function that defines a function called `browser` on the `window.os.apps` object having the following functionality:
The `browser` function accepts one parameter `path` and have the following functionality:
 - creates a new root `div` element with the class `browser`
 - call `os.gui.createWindow` with the following parameters: `Browser, created DOM element and store the returned value to constant `win`
 - call `os.gui.toolbar(win)` and store the returned value to constant `toolbar`
 - call `toolbar.addButton ('📁', () => os.gui.createPrompt('Enter folder name', name => os.fs.mkdir(path, name); refresh())`
 - call `toolbar.addButton ('📄', () => os.gui.createPrompt('Enter folder name', name => os.fs.write(path+'/'+ name, ""); refresh())`
 - call `toolbar.addButton ('🗑️', () => os.fs.rm(path); updates path to remove the last iterm after `/` and refresh)`
 - create an internal refresh function that:
  * removes all the children of the root element
  * call `os.gui.updateStatus` on `win` element to `path`
  * store into `files` constant execution of `os.fs.ls`
  * if lenght of path is bigger than 1 then call `os.gui.addIcon` with the exact following parameters: `..`, `'🔙'`, and a callback that updates path to remove the last iterm after `/` and refresh and root DOM element
  * for each file in the `files` array, do the following:
    * save to variable `isFile` the execution of `os.fs.isFile` with the parameter `path + '/' + name`
    * create a callback function that calls if `isFile` call `os.apps.editor` or set path to `path + '/' + name` and call `refresh()`
    * calls `os.gui.addIcon` with the exact following parameters: `name`, `'📄'` if isFile is true, `'📁'` otherwise, callback function and the created root DOM element 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.apps = window.os.apps || {};
    
    window.os.apps.browser = function(path) {
        const root = document.createElement('div');
        root.className = 'browser';
        document.body.appendChild(root);
        
        const win = os.gui.createWindow('Browser', root);
        const toolbar = os.gui.toolbar(win);
        
        toolbar.addButton('📁', () => {
            os.gui.createPrompt('Enter folder name', name => {
                os.fs.mkdir(path, name);
                refresh();
            });
        });
        
        toolbar.addButton('📄', () => {
            os.gui.createPrompt('Enter file name', name => {
                os.fs.write(path + '/' + name, "");
                refresh();
            });
        });
        
        toolbar.addButton('🗑️', () => {
            os.fs.rm(path);
            path = path.substring(0, path.lastIndexOf('/'));
            refresh();
        });
        
        const refresh = () => {
            while (root.firstChild) {
                root.removeChild(root.firstChild);
            }
            
            os.gui.updateStatus(win, path);
            
            const files = os.fs.ls(path);
            
            if (path.length > 1) {
                os.gui.addIcon('..', '🔙', () => {
                    path = path.substring(0, path.lastIndexOf('/'));
                    refresh();
                }, root);
            }
            
            files.forEach(name => {
                const isFile = os.fs.isFile(path + '/' + name);
                
                const callback = isFile ? 
                    () => { os.apps.editor(path + '/' + name); refresh(); } : 
                    () => { path = path + '/' + name; refresh(); };
                
                os.gui.addIcon(name, isFile ? '📄' : '📁', callback, root);
            });
        };
        
        refresh();
    };
})();


```