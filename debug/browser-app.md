## browser-app

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that defines a function called `browser` on the `window.os.apps` object having the following functionality:
The `browser` function accepts one parameter `path` and have the following functionality:
 - creates a new `div` element with the class `browser`
 - call `os.gui.createWindow` with the following parameters: path, created DOM element
 - call `os.fs.ls` and store it in a variable `files`
 - for each file in the `files` array, do the following:
  * save to variable `isFile` the execution of `os.fs.isFile` with the parameter `path + '/' + name`
  * create a callback function that calls if `isFile` call `os.apps.viewer` or `os.apps.browser` otherwise with the parameter `path + '/' + name`
  * calls `os.gui.addIcon` with the following parameters: `name`, `'📄'` if isFile is true, `'📁'` otherwise, callback function and the created DOM element 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.apps = window.os.apps || {};
    
    window.os.apps.browser = function(path) {
        var div = document.createElement('div');
        div.className = 'browser';
        document.body.appendChild(div);
        
        window.os.gui.createWindow(path, div);
        
        var files = window.os.fs.ls(path);
        
        files.forEach(function(name) {
            var isFile = window.os.fs.isFile(path + '/' + name);
            
            var callback = (function(name) {
                return function() {
                    if (isFile) {
                        window.os.apps.viewer(path + '/' + name);
                    } else {
                        window.os.apps.browser(path + '/' + name);
                    }
                };
            })(name);
            
            window.os.gui.addIcon(name, isFile ? '📄' : '📁', callback, div);
        });
    };
})();


```