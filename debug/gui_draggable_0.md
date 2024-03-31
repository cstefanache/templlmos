## gui_draggable_0
### API
<pre style='text-wrap: wrap'>/**
 * Makes an element draggable by a given handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The handle element to initiate the drag operation.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 Implement `makeDraggable` on `window.os.gui` object that takes two parameters root and dragHandleHTMLElement with the following functionality:
 - change absolute position of root by dragging the dragHandleHTMLElement 
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

</pre>
