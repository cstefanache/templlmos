## window

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `createWindow` on the `window.os.gui` object
The `createWindow` function takes four parameters: title, content (as DOM element) and width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
- create a root DOM element with the class `.window`
- call existing `os.gui.utils.setSizeAndCenter` with the root DOM element, width and height
- add `div` placeholders for `.titlePlaceholder`, `.toolbarPlaceholder`, `.contentPlaceholder` and `.statusPlaceholder` to the root DOM element
- execute function `window.os.gui.titleBar` with the title and the root DOM element as the second parameter and append the returned DOM element to the `.titlePlaceholder`
- append the content parameter as dom child to the `.contentPlaceholder`
- create an internal function `bringToFront` that make all `.window` have z-index: 1 and the current root DOM element have z-index: 2
- when root DOM element is clicked call the `bringToFront` function
- append the root dom element to document body
- call bring to front after 20ms
- return the root DOM element 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    if (!window.os.gui.utils) window.os.gui.utils = { setSizeAndCenter: setSizeAndCenter }; // Assuming this exists somewhere else in your code
    
    window.os.gui.createWindow = function(title = "Default Title", content = null, width = 400, height = 300) {
        var root = document.createElement("div");
        root.className = "window";
        
        window.os.gui.utils.setSizeAndCenter(root, width, height);
        
        var titlePlaceholder = document.createElement("div");
        titlePlaceholder.className = "titlePlaceholder";
        root.appendChild(titlePlaceholder);
        
        var toolbarPlaceholder = document.createElement("div");
        toolbarPlaceholder.className = "toolbarPlaceholder";
        root.appendChild(toolbarPlaceholder);
        
        var contentPlaceholder = document.createElement("div");
        contentPlaceholder.className = "contentPlaceholder";
        root.appendChild(contentPlaceholder);
        
        var statusPlaceholder = document.createElement("div");
        statusPlaceholder.className = "statusPlaceholder";
        root.appendChild(statusPlaceholder);
        
        if(typeof window.os.gui.titleBar === 'function') {
            var titleBar = window.os.gui.titleBar(title, root);
            titlePlaceholder.appendChild(titleBar);
        }
        
        if(content && content instanceof Node) {
            contentPlaceholder.appendChild(content);
        }
        
        var bringToFront = function() {
            var windows = document.querySelectorAll(".window");
            for(var i = 0; i < windows.length; i++) {
                windows[i].style.zIndex = 1;
            }
            root.style.zIndex = 2;
        }
        
        root.onclick = bringToFront;
        
        document.body.appendChild(root);
        
        setTimeout(bringToFront, 20);
        
        return root;
    }
})();


```