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
- create an internal function `bringToFront` that make all `.window` elements to be behind the clicked one
- when root DOM element is clicked call the `bringToFront` function
- append the root dom element to document body
- call bring to front after 20ms 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    window.os.gui.createWindow = function(title = "Default Title", content = null, width = 400, height = 300) {
        // create root DOM element with class .window
        let root = document.createElement("div");
        root.className = "window";
        root.style.width = width + "px";
        root.style.height = height + "px";
        
        // add two empty div placeholders .titlePlaceholder and .contentPlaceholder
        let titlePlaceholder = document.createElement("div");
        titlePlaceholder.className = "titlePlaceholder";
        let contentPlaceholder = document.createElement("div");
        contentPlaceholder.className = "contentPlaceholder";
        root.appendChild(titlePlaceholder);
        root.appendChild(contentPlaceholder);
        
        // call window.os.gui.titleBar with title and root DOM element as second parameter and append result to .titlePlaceholder
        if(typeof window.os.gui.titleBar === 'function') {
            let titleBar = window.os.gui.titleBar(title, root);
            titlePlaceholder.appendChild(titleBar);
        } else {
            console.error("Function window.os.gui.titleBar is not defined");
        }
        
        // append content parameter as dom child to .contentPlaceholder
        if(content && content instanceof HTMLElement) {
            contentPlaceholder.appendChild(content);
        } else {
            console.error("Content parameter is not a valid HTML Element");
        }
        
        // create internal function bringToFront
        let bringToFront = function() {
            let windows = document.querySelectorAll(".window");
            windows.forEach(function(win) {
                if(win !== root) {
                    win.style.zIndex = "1";
                }
            });
            root.style.zIndex = "2";
        };
        
        // when root DOM element is clicked call bringToFront function
        root.addEventListener("click", bringToFront);
        
        // append root dom element to document body
        document.body.appendChild(root);
        
        // call bring to front after 20ms 
        setTimeout(bringToFront, 20);
    };
})();


```