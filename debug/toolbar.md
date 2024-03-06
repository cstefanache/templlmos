## toolbar

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `toolbar` on the `window.os.gui` object
The `toolbar` receives a parameter rootElement as DOM element
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from passed rootElement as parameter
- return an object with the following functions:
  - addButton(text, callback) - add a button to the root DOM element with the text parameter and call the callback when the button is clicked 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    
    window.os.gui.toolbar = function(rootElement) {
        var toolbar = document.createElement('div');
        toolbar.className = 'toolbar';
        
        rootElement.querySelector('.toolbarPlaceholder').appendChild(toolbar);
        
        return {
            addButton: function(text, callback) {
                var button = document.createElement('button');
                button.textContent = text;
                button.addEventListener('click', callback);
                toolbar.appendChild(button);
            }
        };
    };
})();


```