## gui_draggable_0
### API

<pre style='text-wrap: wrap'>
/**
 * Makes an element draggable by changing its absolute position when dragging a specified handle.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The element that will be used to drag the root element.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Implement `makeDraggable` on `window.os.gui` object that takes two parameters root and dragHandleHTMLElement with the following functionality:
 - change absolute position of root by dragging the dragHandleHTMLElement
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

</pre>
