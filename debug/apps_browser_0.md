## apps_browser_0
### API
<pre style='text-wrap: wrap'>function browser(win, path = '') { ... }
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

/**
 * Creates an OS icon element for a given path and sets up a callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The callback function to be executed on click.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) { ... }
currentCallback = function() { ... }



1. Create a `browser` function that takes a win and path defaulting to '' parameter:
 - create a container dom element with class `browser`
 - set browserPath to path or `''` if path is undefined or not string
 - generate internal load function that takes path parameter:
   - set browserPath to path
   - removes all children of the container element
   - if path is not empty, create a new `div` with class icon, inner element `.emoji` with internal span element having content '🔙'  and class `emoji` and on click call load with `path.split('/').slice(0, -1).join('/')`
   - ls all files in the path and for each item:
      - call `getOsIcon` with path+'/'+item and load function as callback
      - add a checkbox with value path+'/'+item that prevent event bubbling
 - execute load on browserPath variable
 - create toolbar
 - call `addButton` on the toolbar with `📁` text and prompt for a name and call mkdir on current browserPath and provided name
 - call `addButton` on the toolbar with `📄` text and prompt for a name and call write on current browserPath and provided name and '' as content
 - call `addButton` on the toolbar with `🗑️` text and list all the selected checkbox values, removes them and calls load on the current path
 - return dom element
</pre>
### Output
<pre style='text-wrap: wrap'>function browser(win, path = '') {
    const container = document.createElement('div');
    container.className = 'browser';
    let browserPath = typeof path === 'string' ? path : '';

    function load(path) {
        browserPath = path;
        container.innerHTML = '';

        if (path) {
            const backIcon = document.createElement('div');
            backIcon.className = 'icon';
            const emojiSpan = document.createElement('span');
            emojiSpan.className = 'emoji';
            emojiSpan.textContent = '🔙';
            backIcon.appendChild(emojiSpan);
            backIcon.onclick = () => load(path.split('/').slice(0, -1).join('/'));
            container.appendChild(backIcon);
        }

        const entries = window.os.fs.ls(path);
        entries.forEach(item => {
            const icon = window.os.getOSIcon(path + '/' + item, () => load(path + '/' + item));
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = path + '/' + item;
            checkbox.onclick = (e) => e.stopPropagation();
            container.appendChild(icon);
            container.appendChild(checkbox);
        });
    }

    load(browserPath);

    const toolbar = window.os.gui.createToolbar(win);
    toolbar('📁', () => {
        const name = prompt('Enter directory name:');
        if (name) {
            window.os.fs.mkdir(browserPath + '/' + name);
            load(browserPath);
        }
    });
    toolbar('📄', () => {
        const name = prompt('Enter file name:');
        if (name) {
            window.os.fs.write(browserPath + '/' + name, '');
            load(browserPath);
        }
    });
    toolbar('🗑️', () => {
        const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
        checkboxes.forEach(checkbox => {
            window.os.fs.rm(checkbox.value);
        });
        load(browserPath);
    });

    return container;
}
</pre>
