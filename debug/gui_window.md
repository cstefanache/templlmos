## gui_window
### API
<pre style='text-wrap: wrap'>The method signature for the `window.os.gui.createWindow` function is as follows:

```javascript
window.os.gui.createWindow : (string, string, function, number, number) => HTMLElement

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The provided code defines a JavaScript function named `titleBar` under the namespace `window.os.gui`. The function creates a title bar element with a title, a close button, and appends it to a parent element. Here are the method signatures for this function:

```javascript
/**
 * Creates a title bar element with a title, a close button, and appends it to a parent element.
 * @param {HTMLElement} parentElement - The parent element to append the title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {function} close - The callback function to execute when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) { ... };

```Here are the function signatures prefixed with `window.os.gui`:

```javascript
window.os.gui.makeDraggable = function (root, dragHandle) {}
window.os.gui.makeResizable = function (root, resizeHandleDOMElement) {}
window.os.gui.bringToFront = function (rootDomNode) {}

``` 

 Define a function called `window.os.gui.createWindow` that takes four parameters: emoji, title, appCallback and width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
- create a root DOM element with the class `.window`, no styles, and add it to document body in the middle of the document
- call bringToFront on the root element
- add and empty div with class `titlePlaceholder` to the root DOM element
- add and empty div with class `toolbarPlaceholder` to the root DOM element
- add and empty div with class `contentPlaceholder` to the root DOM element
- add and empty div with class `statusPlaceholder` to the root DOM element
- add a resize handle to the root DOM element with class `resizeHandle`
- add titleBar to `.titlePlaceholder` having the text `emoji + title` and close callback removes root DOM element from the document body
- append to `contentPlacheolder` the execution of appCallback with the root element as parameter to it
- call makeDraggable on root element by the `.titlePlaceholder` element
- make root element resizable by the `resizeHandle` element
- return root DOM element 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can define this function in JavaScript:

```javascript
window.os.gui.createWindow = function(emoji = "🖥️", title = "New Window", appCallback = () => {}, width = 400, height = 300) {
    // Create root DOM element
    let root = document.createElement("div");
    root.classList.add("window");
    document.body.appendChild(root);
    
    // Bring window to front
    window.os.gui.bringToFront(root);
    
    // Create placeholders for title bar, toolbar, content, status
    let titlePlaceholder = document.createElement("div");
    titlePlaceholder.classList.add("titlePlaceholder");
    root.appendChild(titlePlaceholder);
    
    let toolbarPlaceholder = document.createElement("div");
    toolbarPlaceholder.classList.add("toolbarPlaceholder");
    root.appendChild(toolbarPlaceholder);
    
    let contentPlaceholder = document.createElement("div");
    contentPlaceholder.classList.add("contentPlaceholder");
    root.appendChild(contentPlaceholder);
    
    let statusPlaceholder = document.createElement("div");
    statusPlaceholder.classList.add("statusPlaceholder");
    root.appendChild(statusPlaceholder);
    
    // Create resize handle
    let resizeHandle = document.createElement("div");
    resizeHandle.classList.add("resizeHandle");
    root.appendChild(resizeHandle);
    
    // Create title bar
    window.os.gui.titleBar(titlePlaceholder, emoji + " " + title, () => { document.body.removeChild(root); });
    
    // Append appCallback to content placeholder
    contentPlaceholder.appendChild(appCallback(root));
    
    // Make window draggable by title placeholder
    window.os.gui.makeDraggable(root, titlePlaceholder);
    
    // Make window resizable by resize handle
    window.os.gui.makeResizable(root, resizeHandle);
    
    // Set width and height of root element
    root.style.width = width + "px";
    root.style.height = height + "px";
    
    return root;
};

```</pre>
