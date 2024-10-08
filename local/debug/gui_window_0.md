## gui_window_0
### API
<pre style='text-wrap: wrap'>/**
* Create a new window with given emoji, title, width and height.
* @param {string} emoji - The emoji to display in the window's title bar.
* @param {string} title - The title to display in the window's title bar.
* @param {number} [width=400] - The width of the window in pixels.
* @param {number} [height=300] - The height of the window in pixels.
* @return {HTMLElement} The root DOM element of the newly created window.
*/
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Creates a title bar with a title and a close button.
 * @param {HTMLElement} parentElement - The DOM element to append this title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {function} close - The callback to call when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) { ... }

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
/**
* Brings the specified DOM node to the front of its siblings.
* @param {HTMLElement} rootDOMNode - The DOM node to bring to front.
*/
window.os.gui.bringToFront = function(rootDOMNode) { ... }



 Define a function `createWindow` on the `window.os.gui` object that takes four parameters: emoji, title, width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
- create a root DOM element with the class `.window`, set the width and height only, and add it to document body in the middle of the document
- call bringToFront on the root element
- add and empty div with class `titlePlaceholder` to the root DOM element
- add and empty div with class `toolbarPlaceholder` to the root DOM element
- add and empty div with class `contentPlaceholder` to the root DOM element
- add and empty div with class `statusPlaceholder` to the root DOM element
- add a resize handle to the root DOM element with class `resizeHandle`
- add titleBar to `.titlePlaceholder` having the text `emoji + title` and close callback removes root DOM element from the document body
- make root element draggable by the `.titlePlaceholder` element
- make root element resizable by the `resizeHandle` element
- set root DOM element left position document width divided by 2 minus width divided by 2
- set root DOM element top position document height divided by 2 minus height divided by 2
- return root DOM element 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
* Create a new window with given emoji, title, width and height.
* @param {string} emoji - The emoji to display in the window's title bar.
* @param {string} title - The title to display in the window's title bar.
* @param {number} [width=400] - The width of the window in pixels.
* @param {number} [height=300] - The height of the window in pixels.
* @return {HTMLElement} The root DOM element of the newly created window.
*/
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) {
    // Create root DOM element
    const root = document.createElement('div');
    root.className = 'window';
    root.style.width = `${width}px`;
    root.style.height = `${height}px`;
    document.body.appendChild(root);
    
    // Bring to front
    window.os.gui.bringToFront(root);
    
    // Create placeholders for title bar, toolbar, content, status
    ['titlePlaceholder', 'toolbarPlaceholder', 'contentPlaceholder', 'statusPlaceholder'].forEach(className => {
        const placeholder = document.createElement('div');
        placeholder.className = className;
        root.appendChild(placeholder);
    });
    
    // Create resize handle
    const resizeHandle = document.createElement('div');
    resizeHandle.className = 'resizeHandle';
    root.appendChild(resizeHandle);
    
    // Create title bar
    window.os.gui.titleBar(root.querySelector('.titlePlaceholder'), emoji + ' ' + title, () => document.body.removeChild(root));
    
    // Make window draggable by title bar
    window.os.gui.makeDraggable(root, root.querySelector('.titlePlaceholder'));
    
    // Make window resizable by resize handle
    window.os.gui.makeResizable(root, resizeHandle);
    
    // Position window in center of document
    root.style.position = 'absolute';
    root.style.left = `${window.innerWidth / 2 - width / 2}px`;
    root.style.top = `${window.innerHeight / 2 - height / 2}px`;
    
    return root;
};

</pre>
