## gui_draggable_0
### API
<pre style='text-wrap: wrap'>/**
 * Makes an element draggable by changing its absolute position based on the dragging of a handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The element that will be used to drag the root element.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Implement `makeDraggable` on `window.os.gui` object that takes two parameters root and dragHandleHTMLElement with the following functionality:
 - change absolute position of root by dragging the dragHandleHTMLElement
</pre>
### Output
<pre style='text-wrap: wrap'>window.os = window.os || {};
window.os.gui = window.os.gui || {};

/**
 * Makes an element draggable by changing its absolute position based on the dragging of a handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The element that will be used to drag the root element.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) {
    let offset = { x: 0, y: 0 };
    let isDragging = false;

    dragHandleHTMLElement.addEventListener('mousedown', function(e) {
        isDragging = true;
        offset.x = e.clientX - root.getBoundingClientRect().left;
        offset.y = e.clientY - root.getBoundingClientRect().top;
        document.body.style.userSelect = 'none'; // Prevent text selection
    });

    document.addEventListener('mousemove', function(e) {
        if (isDragging) {
            root.style.position = 'absolute';
            root.style.left = (e.clientX - offset.x) + 'px';
            root.style.top = (e.clientY - offset.y) + 'px';
        }
    });

    document.addEventListener('mouseup', function() {
        isDragging = false;
        document.body.style.userSelect = ''; // Restore text selection
    });
};
</pre>
