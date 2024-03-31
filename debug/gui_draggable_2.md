## gui_draggable_2
### API
<pre style='text-wrap: wrap'>/**
* Brings the specified DOM node to the front of its siblings.
* @param {HTMLElement} rootDOMNode - The DOM node to bring to front.
*/
window.os.gui.bringToFront = function(rootDOMNode) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Makes an element draggable by a given handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The handle element to initiate the drag operation.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) { ... }
/**
* Makes an element resizable by a given handle element.
* @param {HTMLElement} root - The element to be made resizable.
* @param {HTMLElement} resizeHandleHTMLElement - The handle element to initiate the resize operation.
*/
window.os.gui.makeResizable = function(root, resizeHandleHTMLElement) { ... }


 Implement `bringToFront` on `window.os.gui` object that taskes a single parameter: rootDOMNode  with the following functionality:
- creates an internal function that:
  * takes all elements with the same class as rootDomNode
  * iterate through them and sets the z-index to 0 and at the end sets the z-index of rootDOMNode to 1
- adds a mousedown event listener to rootDOMNode that calls the internal function
- call the internal function 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

/**
 * Makes an element draggable by a given handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The handle element to initiate the drag operation.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) {
    let isDragging = false;
    let offsetX = 0;
    let offsetY = 0;
    
    const handleMouseDown = (event) => {
        isDragging = true;
        offsetX = event.clientX - root.getBoundingClientRect().left;
        offsetY = event.clientY - root.getBoundingClientRect().top;
        
        document.addEventListener('mousemove', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);
    };
    
    const handleMouseMove = (event) => {
        if (isDragging) {
            const x = event.clientX - offsetX;
            const y = event.clientY - offsetY;
            
            // Prevent the element from being dragged off the screen
            const boundingRect = document.body.getBoundingClientRect();
            const rootRect = root.getBoundingClientRect();
            if (x < boundingRect.left || y < boundingRect.top || x + rootRect.width > boundingRect.right || y + rootRect.height > boundingRect.bottom) {
                return;
            }
            
            root.style.left = `${x}px`;
            root.style.top = `${y}px`;
        }
    };
    
    const handleMouseUp = () => {
        isDragging = false;
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
    };
    
    dragHandleHTMLElement.addEventListener('mousedown', handleMouseDown);
};

/**
* Makes an element resizable by a given handle element.
* @param {HTMLElement} root - The element to be made resizable.
* @param {HTMLElement} resizeHandleHTMLElement - The handle element to initiate the resize operation.
*/
window.os.gui.makeResizable = function(root, resizeHandleHTMLElement) {
    let startWidth = root.offsetWidth;
    let startHeight = root.offsetHeight;
    let startX;
    let startY;
    
    resizeHandleHTMLElement.addEventListener('mousedown', (e) => {
        e.preventDefault();
        startX = e.clientX;
        startY = e.clientY;
        
        document.addEventListener('mousemove', resize);
        document.addEventListener('mouseup', stopResize);
    });
    
    function resize(e) {
        let width = startWidth + (e.clientX - startX);
        let height = startHeight + (e.clientY - startY);
        
        // Ensure width and height are not negative
        width = Math.max(width, 0);
        height = Math.max(height, 0);
        
        // Update width and height of root element
        root.style.width = width + 'px';
        root.style.height = height + 'px';
    }
    
    function stopResize() {
        // Update starting width and height on mouseup
        startWidth = root.offsetWidth;
        startHeight = root.offsetHeight;
        
        // Remove event listeners
        document.removeEventListener('mousemove', resize);
        document.removeEventListener('mouseup', stopResize);
    }
};

/**
* Brings the specified DOM node to the front of its siblings.
* @param {HTMLElement} rootDOMNode - The DOM node to bring to front.
*/
window.os.gui.bringToFront = function(rootDOMNode) {
    // Internal function to bring to front
    var bringToFront = function() {
        // Get all elements with same class as rootDOMNode
        var siblings = document.getElementsByClassName(rootDOMNode.className);
        // Iterate through them and set z-index to 0
        for (var i = 0; i < siblings.length; i++) {
            siblings[i].style.zIndex = 0;
        }
        // Set z-index of rootDOMNode to 1
        rootDOMNode.style.zIndex = 1;
    };
    
    // Call internal function on mousedown event of rootDOMNode
    rootDOMNode.addEventListener('mousedown', bringToFront);
    
    // Call internal function immediately to bring to front on load
    bringToFront();
};

</pre>
