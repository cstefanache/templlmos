## gui_draggable_2
### API
<pre style='text-wrap: wrap'>/**
 * Brings the specified DOM node to the front by adjusting its z-index.
 * @param {HTMLElement} rootDOMNode - The element to be brought to the front.
 */
window.os.gui.bringToFront = function(rootDOMNode) { ... }
const bringToFrontInternal = function() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Given the following implemented functions:
/**
 * Makes an element draggable by changing its absolute position based on the dragging of a handle element.
 * @param {HTMLElement} root - The element to be made draggable.
 * @param {HTMLElement} dragHandleHTMLElement - The element that will be used to drag the root element.
 */
window.os.gui.makeDraggable = function(root, dragHandleHTMLElement) { ... }
/**
 * Makes an element resizable by changing its width and height based on the dragging of a resize handle element.
 * @param {HTMLElement} root - The element to be made resizable.
 * @param {HTMLElement} resizeHandleHTMLElement - The element that will be used to resize the root element.
 */
window.os.gui.makeResizable = function(root, resizeHandleHTMLElement) { ... }


Implement `bringToFront` on `window.os.gui` object that taskes a single parameter: rootDOMNode  with the following functionality:
- creates an internal function that:
  * takes all elements with the same class as rootDomNode
  * iterate through them and sets the z-index to 0 and at the end sets the z-index of rootDOMNode to 1
- adds a mousedown event listener to rootDOMNode that calls the internal function
- call the internal function
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
/**
 * Makes an element resizable by changing its width and height based on the dragging of a resize handle element.
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
/**
 * Brings the specified DOM node to the front by adjusting its z-index.
 * @param {HTMLElement} rootDOMNode - The element to be brought to the front.
 */
window.os.gui.bringToFront = function(rootDOMNode) {
    const bringToFrontInternal = function() {
        const elements = document.getElementsByClassName(rootDOMNode.className);
        for (let i = 0; i < elements.length; i++) {
            elements[i].style.zIndex = 0;
        }
        rootDOMNode.style.zIndex = 1;
    };

    rootDOMNode.addEventListener('mousedown', bringToFrontInternal);
    bringToFrontInternal();
};
</pre>
