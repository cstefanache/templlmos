## window-utils

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines the following functions on `window.os.gui` object:
- updateStatus(win, value) - update innerText of `.statusPlaceholder` of the win DOM element as parameter with the value parameter 
### Response:

```

```
(function() {
    // Check if window.os exists and is an object
    if (typeof window.os === 'undefined' || typeof window.os !== 'object') {
        window.os = {};
    }
    
    // Check if window.os.gui exists and is an object
    if (typeof window.os.gui === 'undefined' || typeof window.os.gui !== 'object') {
        window.os.gui = {};
    }
    
    // Define the updateStatus function
    window.os.gui.updateStatus = function(win, value) {
        var statusElement = win.querySelector('.statusPlaceholder');
        if (statusElement !== null && statusElement !== undefined) {
            statusElement.innerText = value;
        } else {
            console.error('Element with class .statusPlaceholder not found in provided win DOM element');
        }
    };
})();


```