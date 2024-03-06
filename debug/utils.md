## utils

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines an object `utils` on `window.os.gui` object providing the following functions:
- setSizeAndCenter(root, width, height) - set the root DOM element size to width and height and center root DOM element on the screen 
### Response:

```

```
(function() {
    if (!window.os || !window.os.gui) {
        window.os = window.os || {};
        window.os.gui = window.os.gui || {};
    }
    
    window.os.gui.utils = {
        setSizeAndCenter: function (root, width, height) {
            root.style.width = width + 'px';
            root.style.height = height + 'px';
            
            root.style.position = 'absolute';
            root.style.top = '50%';
            root.style.left = '50%';
            root.style.transform = 'translate(-50%, -50%)';
        }
    };
})();


```