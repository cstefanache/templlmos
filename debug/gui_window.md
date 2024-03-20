## gui_window
### Instruction: 0
<pre style='text-wrap: wrap'>The method signature for the `window.os.gui.titleBar` function is as follows:

```javascript
function titleBar(parentElement, title)

```The provided JavaScript code defines four functions on the `window.os.gui` object: 

1. `makeDraggable(root, dragHandle)`: This function makes an element draggable by setting up event listeners for mouse events that allow for dragging of the element when the drag handle (provided as an argument to the function) is clicked and dragged over. The element's position is updated in real-time as the mouse moves, and it stops being dragged when the mouse button is released.

2. `makeResizable(root, resizeHandle)`: This function makes an element resizable by setting up event listeners for mouse events that allow for resizing of the element when the resize handle (provided as an argument to the function) is clicked and dragged over. The element's width and height are updated in real-time as the mouse moves, and it stops being resized when the mouse button is released.

3. `bringToFront(rootDomNode)`: This function brings a specified DOM node to the front of other nodes with the same class by setting their z-index to 0, then setting the z-index of the rootDomNode to 1. This effectively places it in front of all other nodes with the same class.

4. The last part of your code checks if the `window.os` and `window.os.gui` objects exist, creating them if they don't, before assigning these four functions to them. This ensures that these objects exist before any of these functions are called, preventing potential errors if they are called before these objects are initialized. 

In summary, this code provides a set of utility functions for creating draggable, resizable, and front-bringing elements in a web page, which can be useful for creating user interfaces or other interactive web applications.

``` Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Define a function called `window.os.gui.createWindow` that takes four parameters: emoji, title, content (as DOM element) and width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
- create a root DOM element with the class `.window` and add it to document body
- call bringToFront on the root element
- add and empty div with class `titlePlaceholder` to the root DOM element
- add and empty div with class `toolbarPlaceholder` to the root DOM element
- add and empty div with class `contentPlaceholder` to the root DOM element and append the content parameter to it
- add and empty div with class `statusPlaceholder` to the root DOM element
- add a resize handle to the root DOM element with class `resizeHandle`
- add titleBar to `titlePlaceholder` having the text `emoji + title`
- call makeDraggable on root element by the titlePlaceholder element
- make root element resizable by the resizeHandle element
- return null 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here's how you can define this function in vanilla JavaScript:

```javascript
// Check if window.os and window.os.gui exist, create them if not
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Define createWindow function
window.os.gui.createWindow = function (emoji = '🖥️', title = 'New Window', content = null, width = 400, height = 300) {
    // Create root DOM element with class .window and add it to document body
    const root = document.createElement('div');
    root.classList.add('window');
    document.body.appendChild(root);
    
    // Call bringToFront on root element
    window.os.gui.bringToFront(root);
    
    // Add and empty div with class titlePlaceholder to root DOM element
    const titlePlaceholder = document.createElement('div');
    titlePlaceholder.classList.add('titlePlaceholder');
    root.appendChild(titlePlaceholder);
    
    // Add and empty div with class toolbarPlaceholder to root DOM element
    const toolbarPlaceholder = document.createElement('div');
    toolbarPlaceholder.classList.add('toolbarPlaceholder');
    root.appendChild(toolbarPlaceholder);
    
    // Add and empty div with class contentPlaceholder to root DOM element and append content parameter to it
    const contentPlaceholder = document.createElement('div');
    contentPlaceholder.classList.add('contentPlaceholder');
    root.appendChild(contentPlaceholder);
    if (content !== null) {
        contentPlaceholder.appendChild(content);
    }
    
    // Add and empty div with class statusPlaceholder to root DOM element
    const statusPlaceholder = document.createElement('div');
    statusPlaceholder.classList.add('statusPlaceholder');
    root.appendChild(statusPlaceholder);
    
    // Add resize handle to root DOM element with class resizeHandle
    const resizeHandle = document.createElement('div');
    resizeHandle.classList.add('resizeHandle');
    root.appendChild(resizeHandle);
    
    // Add titleBar to titlePlaceholder having text emoji + title
    window.os.gui.titleBar(titlePlaceholder, emoji + ' ' + title);
    
    // Call makeDraggable on root element by the titlePlaceholder element
    window.os.gui.makeDraggable(root, titlePlaceholder);
    
    // Make root element resizable by resizeHandle element
    window.os.gui.makeResizable(root, resizeHandle);
    
    // Set default width and height of root element
    root.style.width = width + 'px';
    root.style.height = height + 'px';
    
    // Return null
    return null;
}

```</pre>
### Library
<pre style='text-wrap: wrap'>The function `window.os.gui.createWindow` is a JavaScript function that creates a new GUI window with various components such as title bar, toolbar, content area, status bar, and a resize handle. The function takes in several parameters including emoji for the title bar, title of the window, content to be displayed in the content area, width of the window, and height of the window. The function returns null after creating the window. 

Here is the function signature:

```javascript
window.os.gui.createWindow(emoji?: string, title?: string, content?: Node | null, width?: number, height?: number): null;

```</pre>
