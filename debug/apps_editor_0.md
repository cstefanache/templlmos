## apps_editor_0
### API
<pre style='text-wrap: wrap'>function editor(win, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.

Given the following implemented functions:
    /**
     * Saves the filesystem object to local storage.
     * @function
     */
window.os.fs.sync = function() { ... }
    /**
     * Processes and returns a path, handling '..', '//' and '/'.
     * @param {string} path - The path to process.
     * @returns {string|null} - The processed path or null if invalid.
     */
window.os.fs.getPath = function(path) { ... }
    /**
     * Checks if the path is valid.
     * @param {string} path - The path to check.
     * @returns {boolean} - True if valid, false otherwise.
     */
window.os.fs.isValidPath = function(path) { ... }
    /**
     * Returns a list of entries in the filesystem object at the given path.
     * @param {string} path - The path to list entries from.
     * @returns {Array} - An array of entries.
     */
window.os.fs.ls = function(path) { ... }
    /**
     * Creates an empty object at the given path.
     * @param {string} path - The path to create the directory at.
     */
window.os.fs.mkdir = function(path) { ... }
    /**
     * Removes the object at the given path.
     * @param {string} path - The path to remove the object from.
     */
window.os.fs.rm = function(path) { ... }
    /**
     * Writes the content to an entry in the filesystem object at the given path.
     * @param {string} path - The path to write to.
     * @param {string} content - The content to write.
     */
window.os.fs.write = function(path, content) { ... }
    /**
     * Reads an entry split by '\n' in the filesystem object at the given path.
     * @param {string} path - The path to read from.
     * @returns {Array|null} - An array of lines or null if not found.
     */
window.os.fs.read = function(path) { ... }

/**
 * Creates a toolbar and appends it to the specified window element.
 * @param {HTMLElement} win - The window element to which the toolbar will be appended.
 * @returns {function(string, function): void} - A function to add buttons to the toolbar.
 */
window.os.gui.createToolbar = function(win) { ... }
    /**
     * Adds a button to the toolbar.
     * @param {string} text - The text to display on the button.
     * @param {function} callback - The function to call when the button is clicked.
     */

/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to display for the application.
 * @param {Function} callback - The function to call when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions=undefined] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions = undefined) { ... }



Create a `editor` function that takes a window and path parameter:
 - create a dom element with class `editor`
 - add a textarea element to the previously created element 100% width and 100% height
 - save reference to the textarea element
 - create toolbar on the `window` parameter
 - if path is not empty, read the file content and set it to the textarea
 - add button to the toolbar with `💾` text save textarea content to the path if path is defined, prompt for the path otherwise
 - return  dom element

call register application with 'Editor' title, ✍️ as emoji, `editor` function reference and 400x450 size for [txt,doc] extensions
</pre>
### Output
<pre style='text-wrap: wrap'>function editor(win, path) {
    const editorElement = document.createElement('div');
    editorElement.className = 'editor';

    const textarea = document.createElement('textarea');
    textarea.style.width = '100%';
    textarea.style.height = '100%';
    editorElement.appendChild(textarea);

    const toolbar = window.os.gui.createToolbar(win);

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            textarea.value = content.join('\n');
        }
    }

    toolbar('💾', function() {
        const savePath = path || prompt('Enter the path to save the file:');
        if (savePath) {
            window.os.fs.write(savePath, textarea.value);
        }
    });

    return editorElement;
}

window.os.registerApplication('Editor', '✍️', editor, 400, 450, ['txt', 'doc']);
</pre>
