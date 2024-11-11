## gui_window_0
### API
<pre style='text-wrap: wrap'>/**
 * Creates a new window with a title, emoji, and specified dimensions.
 * @param {string} emoji - The emoji to display in the title.
 * @param {string} title - The title of the window.
 * @param {number} [width=400] - The width of the window.
 * @param {number} [height=300] - The height of the window.
 * @returns {HTMLElement} The created window element.
 */
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Define a function `createWindow` on the `window.os.gui` object that takes four parameters: emoji, title, width and height that are defaulting to 400 and 300, respectively if not passed and have the following functionality:
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
- return root DOM element</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Creates a new window with a title, emoji, and specified dimensions.
 * @param {string} emoji - The emoji to display in the title.
 * @param {string} title - The title of the window.
 * @param {number} [width=400] - The width of the window.
 * @param {number} [height=300] - The height of the window.
 * @returns {HTMLElement} The created window element.
 */
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) {
    const root = document.createElement('div');
    root.className = 'window';
    root.style.width = `${width}px`;
    root.style.height = `${height}px`;
    root.style.position = 'absolute';
    root.style.left = `${(window.innerWidth / 2) - (width / 2)}px`;
    root.style.top = `${(window.innerHeight / 2) - (height / 2)}px`;
    
    window.os.gui.bringToFront(root);
    
    const titlePlaceholder = document.createElement('div');
    titlePlaceholder.className = 'titlePlaceholder';
    root.appendChild(titlePlaceholder);
    
    const toolbarPlaceholder = document.createElement('div');
    toolbarPlaceholder.className = 'toolbarPlaceholder';
    root.appendChild(toolbarPlaceholder);
    
    const contentPlaceholder = document.createElement('div');
    contentPlaceholder.className = 'contentPlaceholder';
    root.appendChild(contentPlaceholder);
    
    const statusPlaceholder = document.createElement('div');
    statusPlaceholder.className = 'statusPlaceholder';
    root.appendChild(statusPlaceholder);
    
    const resizeHandle = document.createElement('div');
    resizeHandle.className = 'resizeHandle';
    root.appendChild(resizeHandle);
    
    window.os.gui.titleBar(titlePlaceholder, `${emoji} ${title}`, function() {
        document.body.removeChild(root);
    });
    
    window.os.gui.makeDraggable(root, titlePlaceholder);
    window.os.gui.makeResizable(root, resizeHandle);
    
    document.body.appendChild(root);
    return root;
};
</pre>
