## viwer-app

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that defines a function called `viewer` on the `window.os.apps` object having the following functionality:
The `viewer` function accepts one parameter `path` and have the following functionality:
 - creates a new `div` element with the class `viewer`
 - call `os.gui.createWindow` with the following parameters: path, created DOM element
 - call `os.fs.readPath` with the parameter `path` and store it in a variable `content`
 - create a new `pre` element with the class `content` and set its innerHTML to `content`
 - append the `pre` element to the created DOM element 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.apps = window.os.apps || {};
    
    window.os.apps.viewer = function(path) {
        var div = document.createElement('div');
        div.className = 'viewer';
        document.body.appendChild(div);
        
        window.os.gui.createWindow(path, div);
        
        var content = window.os.fs.readPath(path);
        
        var pre = document.createElement('pre');
        pre.className = 'content';
        pre.innerHTML = content;
        div.appendChild(pre);
    };
})();


```