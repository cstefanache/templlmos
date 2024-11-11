## gui_window_1
### API
<pre style='text-wrap: wrap'>/**
 * Attaches a content element to the content placeholder of a window element.
 * @param {HTMLElement} windowElement - The window element to which the content will be attached.
 * @param {HTMLElement} contentElement - The content element to be appended to the window's content placeholder.
 */
window.os.gui.attachToWindow = function(windowElement, contentElement) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Define a function called `attachToWindow` on the `window.os.gui` object that takes two parameters: windowElement and contentElement that takes the contentElement and appends it to the `.contentPlaceholder` of the windowElement</pre>
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
/**
 * Attaches a content element to the content placeholder of a window element.
 * @param {HTMLElement} windowElement - The window element to which the content will be attached.
 * @param {HTMLElement} contentElement - The content element to be appended to the window's content placeholder.
 */
window.os.gui.attachToWindow = function(windowElement, contentElement) {
    const contentPlaceholder = windowElement.querySelector('.contentPlaceholder');
    if (contentPlaceholder) {
        contentPlaceholder.appendChild(contentElement);
    }
};
</pre>
