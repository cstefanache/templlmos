## apps_editor_0
### API
<pre style='text-wrap: wrap'>function editor(win, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Save the filesystem object to localStorage
 */
window.os.fs.sync = function() { ... }
/**
 * Get file content at given path
 * @param {string} path - The path to the file
 * @returns {string|undefined} - The content of the file or undefined if not found
 */
window.os.fs.getFileContentFromPath = function(path) { ... }
/**
 * Write content to a file at given path
 * @param {string} path - The path to the file
 * @param {string} content - The content to write to the file
 */
window.os.fs.write = function(path, content) { ... }
/**
 * List entries at given path
 * @param {string} path - The path to list entries at
 * @returns {Array} - An array of entries at the path or root if path is not found
 */
window.os.fs.ls = function(path = '') { ... }
/**
 * Create a directory at given path
 * @param {string} path - The path to create a directory at
 */
window.os.fs.mkdir = function(path) { ... }
/**
 * Remove a file or directory at given path
 * @param {string} path - The path to remove at
 */
window.os.fs.rm = function(path) { ... }
/**
 * Check if a path is a file
 * @param {string} path - The path to check
 * @returns {boolean} - True if path is a file, false otherwise
 */
window.os.fs.isFile = function(path) { ... }

/**
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) { ... }

/**
 * Register an application on the desktop.
 * 
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 * @param {number} [width=400] - The width of the application's window in pixels.
 * @param {number} [height=400] - The height of the application's window in pixels.
 * @param {Array<string>} [extensions] - The file extensions to register for this application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) { ... }



 Create a `editor` function that takes a window and path parameter:
 - create a dom element with class `editor`
 - add a textarea element to the previously created element 100% width and 100% height
 - save reference to the textarea element
 - create toolbar on the `window` parameter
 - if path is not empty, read the file content and set it to the textarea
 - add button on the toolbar with `💾` text save textarea content to the path if path is defined, prompt for the path otherwise
 - return  dom element

call register application with 'Editor' title, ✍️ as emoji, `editor` function reference and 400x450 size for [txt,doc] extensions 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>function editor(win, path) {
    // Create a div element with class 'editor'
    const editorDiv = document.createElement('div');
    editorDiv.className = 'editor';
    
    // Create a textarea element with 100% width and height
    const textarea = document.createElement('textarea');
    textarea.style.width = '100%';
    textarea.style.height = '100%';
    
    // Add textarea to editorDiv
    editorDiv.appendChild(textarea);
    
    // Create toolbar on win parameter
    const addButton = window.os.gui.createToolbar(win);
    
    // If path is not empty, read file content and set it to textarea
    if (path) {
        const content = window.os.fs.getFileContentFromPath(path);
        if (content) textarea.value = content;
    }
    
    // Add button on toolbar with '💾' text that saves textarea content to path if path is defined, prompt for path otherwise
    addButton('💾', () => {
        const newPath = path || window.prompt('Enter a path');
        if (newPath) window.os.fs.write(newPath, textarea.value);
    });
    
    // Return editorDiv
    return editorDiv;
}

// Register application with 'Editor' title, ✍️ as emoji, editor function reference and 400x450 size for [txt,doc] extensions 
window.os.registerApplication('Editor', '✍️', editor, 400, 450, ['txt', 'doc']);

</pre>
