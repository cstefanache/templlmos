## gui_draggable_2
### API

<pre style='text-wrap: wrap'>
/**
 * Brings the specified DOM node to the front by adjusting its z-index.
 * @param {HTMLElement} rootDOMNode - The element to be brought to the front.
 */
window.os.gui.bringToFront = function(rootDOMNode) { ... }
const bringToFrontInternal = function() { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Implement `bringToFront` on `window.os.gui` object that taskes a single parameter: rootDOMNode  with the following functionality:
- creates an internal function that:
  * takes all elements with the same class as rootDomNode
  * iterate through them and sets the z-index to 0 and at the end sets the z-index of rootDOMNode to 1
- adds a mousedown event listener to rootDOMNode that calls the internal function
- call the internal function
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
