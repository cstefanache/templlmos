## window

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `createWindow` on the `window.os.gui` object
The `createWindow` function takes four parameters: title, content (as DOM element) and width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
- create a root DOM element with the class `.window`
- add two empty `div` placeholders: `.titlePlaceholder` and `.contentPlaceholder`
- call `window.os.gui.titleBar` with the title and the root DOM element as the second parameter and append the result to the `.titlePlaceholder`
- append the content parameter as dom child to the `.contentPlaceholder`
- append the root dom element to document body 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    
    window.os.gui.createWindow = function(title = "Default Title", content = null, width = 400, height = 300) {
        // create root DOM element with class .window
        var root = document.createElement("div");
        root.className = "window";
        root.style.width = width + "px";
        root.style.height = height + "px";
        
        // add two empty div placeholders .titlePlaceholder and .contentPlaceholder
        var titlePlaceholder = document.createElement("div");
        titlePlaceholder.className = "titlePlaceholder";
        var contentPlaceholder = document.createElement("div");
        contentPlaceholder.className = "contentPlaceholder";
        
        root.appendChild(titlePlaceholder);
        root.appendChild(contentPlaceholder);
        
        // call window.os.gui.titleBar with the title and root DOM element as second parameter and append result to .titlePlaceholder
        if(typeof window.os.gui.titleBar === 'function') {
            var titleBar = window.os.gui.titleBar(title, root);
            titlePlaceholder.appendChild(titleBar);
        } else {
            console.error("Function window.os.gui.titleBar is not defined.");
        }
        
        // append content parameter as dom child to .contentPlaceholder
        if(content && content instanceof Node) {
            contentPlaceholder.appendChild(content);
        } else {
            console.error("Content parameter is not a valid DOM node.");
        }
        
        // append root dom element to document body 
        document.body.appendChild(root);
    };
})();


```