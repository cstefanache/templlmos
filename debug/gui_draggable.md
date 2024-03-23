## gui_draggable
### API
<pre style='text-wrap: wrap'>Here are the function signatures prefixed with `window.os.gui`:

```javascript
window.os.gui.makeDraggable = function (root, dragHandle) {}
window.os.gui.makeResizable = function (root, resizeHandleDOMElement) {}
window.os.gui.bringToFront = function (rootDomNode) {}

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>do not use jquery.
 `window.os` object is already defined.
### Instruction:
 Implement the following functions on the `window.os` object under `gui` key:
- `makeDraggable(root, dragHandle)` - drag the root  by dragging the dragHandle element. Both root and dragHandle are DOM elements. 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>You can implement this function using JavaScript's built-in event listeners and properties to handle mouse events and move elements around. Here's a simple implementation of this function:

```javascript
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

window.os.gui.makeDraggable = function (root, dragHandle) {
    var offsetX = 0;
    var offsetY = 0;
    
    dragHandle.addEventListener('mousedown', function (event) {
        offsetX = event.clientX - root.getBoundingClientRect().left;
        offsetY = event.clientY - root.getBoundingClientRect().top;
        
        document.addEventListener('mousemove', move);
        document.addEventListener('mouseup', drop);
    });
    
    function move (event) {
        event.preventDefault();
        root.style.position = 'absolute';
        root.style.left = event.clientX - offsetX + 'px';
        root.style.top = event.clientY - offsetY + 'px';
    }
    
    function drop () {
        document.removeEventListener('mousemove', move);
        document.removeEventListener('mouseup', drop);
    }
};

```</pre>
### Instruction: 2
<pre style='text-wrap: wrap'>do not use jquery.
 `window.os` object is already defined.
### Instruction:
 Implement the following functions on the `window.os` object under `gui` key:
`makeResizable(root, resizeHandleDOMElement) that:` 
 - resize (both width and height) the root element by dragging the resizeHandle DOM element.
 - update starting width and height on mouseup 
### Response:
</pre>
#### Output: 1
<pre style='text-wrap: wrap'>Sure, here's a simple implementation of this function using JavaScript and CSS for resizing. This implementation assumes that you're using a flexbox layout for your root element and a simple div for your resize handle. The handle will be positioned at the bottom right of the root element and will be draggable by the user. When the user releases their mouse button, the dimensions of the root element will be updated to match the current size of the handle.

```javascript
// Add gui namespace if it doesn't exist
if (!window.os || !window.os.gui) {
    window.os = window.os || {};
    window.os.gui = {};
}

// Define makeResizable function
window.os.gui.makeResizable = function (root, resizeHandleDOMElement) {
    let rootRect = root.getBoundingClientRect();
    let startX = rootRect.width;
    let startY = rootRect.height;
    let startMouseX;
    let startMouseY;
    let startRootX = rootRect.x;
    let startRootY = rootRect.y;
    
    // Add event listeners for mousedown and mousemove events
    resizeHandleDOMElement.addEventListener('mousedown', function (e) {
        e.preventDefault();
        startMouseX = e.clientX;
        startMouseY = e.clientY;
        document.addEventListener('mousemove', mouseMove);
        document.addEventListener('mouseup', mouseUp);
    });
    
    // Define mouseMove function
    function mouseMove(e) {
        let diffX = e.clientX - startMouseX;
        let diffY = e.clientY - startMouseY;
        root.style.width = startX + diffX + 'px';
        root.style.height = startY + diffY + 'px';
    }
    
    // Define mouseUp function
    function mouseUp() {
        document.removeEventListener('mousemove', mouseMove);
        document.removeEventListener('mouseup', mouseUp);
        let rootRect = root.getBoundingClientRect();
        startX = rootRect.width;
        startY = rootRect.height;
        startRootX = rootRect.x;
        startRootY = rootRect.y;
    }
};

```</pre>
### Instruction: 3
<pre style='text-wrap: wrap'>do not use jquery.
 `window.os` object is already defined.
### Instruction:
 Implement `bringToFront(rootDOMNode)` on the `window.os.gui` that:
- creates an internal function that:
  * takes all elements with the same class as rootDomNode
  * iterate through them and sets the z-index to 0
  * sets the z-index of rootDOMNode to 1
- adds a mousedown event listener to rootDOMNode that calls the internal function 
### Response:
</pre>
#### Output: 2
<pre style='text-wrap: wrap'>Here's how you can implement this in JavaScript:

```javascript
if (!window.os || !window.os.gui) {
    window.os = window.os || {};
    window.os.gui = window.os.gui || {};
}

window.os.gui.bringToFront = function (rootDomNode) {
    // Internal function to bring other nodes to front
    var bringOthersToFront = function () {
        // Get all nodes with same class as rootDomNode
        var nodes = document.getElementsByClassName(rootDomNode.className);
        // Iterate through them and set z-index to 0
        for (var i = 0; i < nodes.length; i++) {
            nodes[i].style.zIndex = 0;
        }
        // Set z-index of rootDomNode to 1
        rootDomNode.style.zIndex = 1;
    }
    
    // Add mousedown event listener to rootDomNode
    rootDomNode.addEventListener('mousedown', bringOthersToFront);
}

```</pre>
