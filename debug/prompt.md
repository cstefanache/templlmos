## prompt

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `createPrompt` on the `window.os.gui` object
The `prompt` function takes two parameters: title and a callback:
* creates a root dom element with the class `editor`
* add a text input element to the root dom element full width
* add a button element to the root dom element and set the text to `OK`
* call `os.gui.createWindow` with the following parameters: `title` parameter, created root DOM element, `300`, `100` and save the result in a variable named `win`
* when the button is clicked call the callback with the value of the input element and remove the win element from the body 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    
    window.os.gui.createPrompt = function(title, callback) {
        // create root dom element with class 'editor'
        var root = document.createElement('div');
        root.className = 'editor';
        
        // add text input element to root dom element full width
        var input = document.createElement('input');
        input.style.width = '100%';
        root.appendChild(input);
        
        // add button element to root dom element and set text to 'OK'
        var button = document.createElement('button');
        button.textContent = 'OK';
        root.appendChild(button);
        
        // call os.gui.createWindow with given parameters
        var win = window.os.gui.createWindow(title, root, 300, 100);
        
        // when button is clicked, call callback with input value and remove win element from body
        button.addEventListener('click', function() {
            callback(input.value);
            document.body.removeChild(win);
        });
    };
})();


```