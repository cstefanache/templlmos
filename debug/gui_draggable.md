## gui_draggable
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Firstly, we need to check if window.os exists and gui exists inside it. If not, we create them.
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Now we implement makeDraggable function
window.os.gui.makeDraggable = function (root, dragHandleHTMLElement) {
    var isDragging = false; // flag to check if we're currently dragging
    var offsetX = 0; // offset from mouse to element start position
    var offsetY = 0; // offset from mouse to element start position
    
    // function to start dragging
    function startDragging(e) {
        e = e || window.event; // for IE
        e.preventDefault(); // prevent selection of text while dragging
        isDragging = true; // set flag to true
        offsetX = e.clientX - root.getBoundingClientRect().left; // calculate offsets
        offsetY = e.clientY - root.getBoundingClientRect().top;
        document.onmousemove = function (e) { moveElement(e); }; // set mousemove event handler
        document.onmouseup = function () { stopDragging(); }; // set mouseup event handler
    }
    
    // function to move element during dragging
    function moveElement(e) {
        e = e || window.event; // for IE
        if (isDragging) { // if we're currently dragging
            var newX = e.clientX - offsetX; // calculate new position
            var newY = e.clientY - offsetY; // calculate new position
            root.style.left = newX + 'px'; // set new position
            root.style.top = newY + 'px'; // set new position
        }
    }
    
    // function to stop dragging
    function stopDragging() {
        isDragging = false; // set flag to false
        document.onmousemove = null; // remove mousemove event handler
        document.onmouseup = null; // remove mouseup event handler
    }
    
    // add mousedown event listener to drag handle
    dragHandleHTMLElement.addEventListener('mousedown', startDragging);
}

// Create 'gui' namespace if it doesn't exist
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Function to make an element resizable
window.os.gui.makeResizable = function (root, resizeHandleElement) {
    var startX;
    var startY;
    var startWidth = root.offsetWidth;
    var startHeight = root.offsetHeight;
    
    // Function to handle mouse down event
    function handleMouseDown(e) {
        e = e || window.event;
        startX = e.clientX;
        startY = e.clientY;
        document.onmouseup = handleMouseUp;
        document.onmousemove = handleMouseMove;
    }
    
    // Function to handle mouse up event
    function handleMouseUp() {
        document.onmouseup = null;
        document.onmousemove = null;
        startWidth = root.offsetWidth;
        startHeight = root.offsetHeight;
    }
    
    // Function to handle mouse move event
    function handleMouseMove(e) {
        e = e || window.event;
        var diffX = e.clientX - startX;
        var diffY = e.clientY - startY;
        root.style.width = (startWidth + diffX) + 'px';
        root.style.height = (startHeight + diffY) + 'px';
    }
    
    // Add event listeners to handle mouse events
    resizeHandleElement.addEventListener('mousedown', handleMouseDown);
}

// Assuming window.os.gui is already defined
if (!window.os.gui) {
    window.os.gui = {};
}

// Function to bring to front
window.os.gui.bringToFront = function (rootDomNode) {
    // Internal function to set z-index to 0 for all elements with same class as rootDomNode
    var setZIndexToZero = function (className) {
        var elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.zIndex = 0;
        }
    };
    
    // Set z-index of rootDomNode to 1
    rootDomNode.style.zIndex = 1;
    
    // Add mousedown event listener to rootDomNode
    rootDomNode.addEventListener('mousedown', function () {
        setZIndexToZero(rootDomNode.className);
    });
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript code defines several utility functions for GUI manipulation such as making elements draggable, resizable, and bringing elements to front. Here's how you can use these functions:

1. **makeDraggable**: This function makes an element draggable by adding mouse events listeners for mousedown (start dragging), mousemove (move element), and mouseup (stop dragging). The root element is the element you want to make draggable, and dragHandleHTMLElement is the element you want to use as the drag handle. 

Example usage: 
```javascript
var draggableElement = document.getElementById('draggable');
var dragHandle = document.getElementById('drag-handle');
window.os.gui.makeDraggable(draggableElement, dragHandle);
```

2. **makeResizable**: This function makes an element resizable by adding mouse events listeners for mousedown (start resizing), mousemove (resize element), and mouseup (stop resizing). The root element is the element you want to make resizable, and resizeHandleElement is the element you want to use as the resize handle. 

Example usage: 
```javascript
var resizableElement = document.getElementById('resizable');
var resizeHandle = document.getElementById('resize-handle');
window.os.gui.makeResizable(resizableElement, resizeHandle);
```

3. **bringToFront**: This function brings an element to front of other elements with same class name when mousedown event is triggered on rootDomNode. The rootDomNode is the element you want to bring to front. 

Example usage: 
```javascript
var elementToBringToFront = document.getElementById('bring-to-front');
window.os.gui.bringToFront(elementToBringToFront);
```

Please note that these functions assume that you have already defined `window.os` and `window.os.gui` in your script. They will not work without these definitions. Also, these functions manipulate CSS properties directly which may have unintended side effects in some cases. It's always good practice to handle these cases in your own code.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Implement the following functions on the `window.os` object under `gui` key:
- `makeDraggable(root, dragHandleHTMLElement)` - when user is dragging the dragHandleHTMLElement, move the root HTMLElement 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, I can help you with this. Here's how you can implement this in JavaScript using the native DOM events for drag and drop functionality. 

```javascript
// Firstly, we need to check if window.os exists and gui exists inside it. If not, we create them.
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Now we implement makeDraggable function
window.os.gui.makeDraggable = function (root, dragHandleHTMLElement) {
    var isDragging = false; // flag to check if we're currently dragging
    var offsetX = 0; // offset from mouse to element start position
    var offsetY = 0; // offset from mouse to element start position
    
    // function to start dragging
    function startDragging(e) {
        e = e || window.event; // for IE
        e.preventDefault(); // prevent selection of text while dragging
        isDragging = true; // set flag to true
        offsetX = e.clientX - root.getBoundingClientRect().left; // calculate offsets
        offsetY = e.clientY - root.getBoundingClientRect().top;
        document.onmousemove = function (e) { moveElement(e); }; // set mousemove event handler
        document.onmouseup = function () { stopDragging(); }; // set mouseup event handler
    }
    
    // function to move element during dragging
    function moveElement(e) {
        e = e || window.event; // for IE
        if (isDragging) { // if we're currently dragging
            var newX = e.clientX - offsetX; // calculate new position
            var newY = e.clientY - offsetY; // calculate new position
            root.style.left = newX + 'px'; // set new position
            root.style.top = newY + 'px'; // set new position
        }
    }
    
    // function to stop dragging
    function stopDragging() {
        isDragging = false; // set flag to false
        document.onmousemove = null; // remove mousemove event handler
        document.onmouseup = null; // remove mouseup event handler
    }
    
    // add mousedown event listener to drag handle
    dragHandleHTMLElement.addEventListener('mousedown', startDragging);
}

```</pre>
### Instruction: 2
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Implement the following functions on the `window.os` object under `gui` key:
`makeResizable(root, resizeHandleHTMLElement) that:` 
 - resize (both width and height) the root HTMLElement element by dragging the resizeHandle DOM element.
 - update starting width and height on mouseup 
### Response:
</pre>
#### Output: 1
<pre style='text-wrap: wrap'>Sure, here is an example of how you can implement this using plain JavaScript. This code assumes that you have already included jQuery in your project. 

```javascript
// Create 'gui' namespace if it doesn't exist
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Function to make an element resizable
window.os.gui.makeResizable = function (root, resizeHandleElement) {
    var startX;
    var startY;
    var startWidth = root.offsetWidth;
    var startHeight = root.offsetHeight;
    
    // Function to handle mouse down event
    function handleMouseDown(e) {
        e = e || window.event;
        startX = e.clientX;
        startY = e.clientY;
        document.onmouseup = handleMouseUp;
        document.onmousemove = handleMouseMove;
    }
    
    // Function to handle mouse up event
    function handleMouseUp() {
        document.onmouseup = null;
        document.onmousemove = null;
        startWidth = root.offsetWidth;
        startHeight = root.offsetHeight;
    }
    
    // Function to handle mouse move event
    function handleMouseMove(e) {
        e = e || window.event;
        var diffX = e.clientX - startX;
        var diffY = e.clientY - startY;
        root.style.width = (startWidth + diffX) + 'px';
        root.style.height = (startHeight + diffY) + 'px';
    }
    
    // Add event listeners to handle mouse events
    resizeHandleElement.addEventListener('mousedown', handleMouseDown);
}

```</pre>
### Instruction: 3
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
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
<pre style='text-wrap: wrap'>Here is how you can implement this in Javascript:

```javascript
// Assuming window.os.gui is already defined
if (!window.os.gui) {
    window.os.gui = {};
}

// Function to bring to front
window.os.gui.bringToFront = function (rootDomNode) {
    // Internal function to set z-index to 0 for all elements with same class as rootDomNode
    var setZIndexToZero = function (className) {
        var elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.zIndex = 0;
        }
    };
    
    // Set z-index of rootDomNode to 1
    rootDomNode.style.zIndex = 1;
    
    // Add mousedown event listener to rootDomNode
    rootDomNode.addEventListener('mousedown', function () {
        setZIndexToZero(rootDomNode.className);
    });
};

```</pre>
