## gui_draggable_1
### API

<pre style='text-wrap: wrap'>
/**
 * Makes an element resizable by changing its width and height when dragging a specified resize handle.
 * @param {HTMLElement} root - The element to be made resizable.
 * @param {HTMLElement} resizeHandleHTMLElement - The element that will be used to resize the root element.
 */
window.os.gui.makeResizable = function(root, resizeHandleHTMLElement) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Implement `makeResizable` on `window.os.gui` object  that takes two parameters: root, resizeHandleHTMLElement with the following functionality:` 
 - resize (both width and height) the root HTMLElement element by dragging the resizeHandle DOM element.
 - update starting width and height on mouseup
</pre>
### Output

<pre style='text-wrap: wrap'>
window.os = window.os || {};
window.os.gui = window.os.gui || {};

/**
 * Makes an element draggable by changing its absolute position when dragging a specified handle.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The element that will be used to drag the root element.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) {
    let offsetX, offsetY;

    dragHandleHTMLElement.addEventListener('mousedown', function(e) {
        offsetX = e.clientX - root.getBoundingClientRect().left;
        offsetY = e.clientY - root.getBoundingClientRect().top;

        function mouseMoveHandler(e) {
            root.style.position = 'absolute';
            root.style.left = (e.clientX - offsetX) + 'px';
            root.style.top = (e.clientY - offsetY) + 'px';
        }

        function mouseUpHandler() {
            document.removeEventListener('mousemove', mouseMoveHandler);
            document.removeEventListener('mouseup', mouseUpHandler);
        }

        document.addEventListener('mousemove', mouseMoveHandler);
        document.addEventListener('mouseup', mouseUpHandler);
    });
};
/**
 * Makes an element resizable by changing its width and height when dragging a specified resize handle.
 * @param {HTMLElement} root - The element to be made resizable.
 * @param {HTMLElement} resizeHandleHTMLElement - The element that will be used to resize the root element.
 */
window.os = window.os || {};
window.os.gui = window.os.gui || {};

window.os.gui.makeResizable = function(root, resizeHandleHTMLElement) {
    let isResizing = false;
    let lastDownX = 0;
    let lastDownY = 0;
    let startWidth = 0;
    let startHeight = 0;

    resizeHandleHTMLElement.addEventListener('mousedown', function(e) {
        isResizing = true;
        lastDownX = e.clientX;
        lastDownY = e.clientY;
        startWidth = parseInt(document.defaultView.getComputedStyle(root).width, 10);
        startHeight = parseInt(document.defaultView.getComputedStyle(root).height, 10);
        e.preventDefault();
    });

    document.addEventListener('mousemove', function(e) {
        if (!isResizing) return;
        const width = startWidth + (e.clientX - lastDownX);
        const height = startHeight + (e.clientY - lastDownY);
        root.style.width = width + 'px';
        root.style.height = height + 'px';
    });

    document.addEventListener('mouseup', function() {
        isResizing = false;
    });
};

</pre>
