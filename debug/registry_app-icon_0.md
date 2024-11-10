## registry_app-icon_0
### API
<pre style='text-wrap: wrap'>/**
 * Creates an OS icon element for a given path and sets up a callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The callback function to be executed on click.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) { ... }
currentCallback = function() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

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



create jsdoc and function `getOSIcon` on `window.os` object having a path and callback parameter with the following functionality:
- create a root element `div` having the class `icon`
- save isFile to constant
- add a span element with class `emoji` and content 📄 if isFile, 📁 otherwise
- add a div element with class title containing the name from path
- extract extension from path and search if is registered in the `window.os.registry` object
- sets `currentCallback` to function parameter callback
- if extension is registered reads stores it in a `extData` property and:
   - adds span element with class `app-emoji` with the content of `extData.emoji` 
   - sets the `currentCallback` to a function that calls `extData.callback` with the path
- exit condition and add click listener to the root element that calls `currentCallback` with the path
- return the root element
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Creates an OS icon element for a given path and sets up a callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The callback function to be executed on click.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) {
    const iconElement = document.createElement('div');
    iconElement.className = 'icon';

    const isFile = path.includes('.');
    const emojiSpan = document.createElement('span');
    emojiSpan.className = 'emoji';
    emojiSpan.textContent = isFile ? '📄' : '📁';
    iconElement.appendChild(emojiSpan);

    const titleDiv = document.createElement('div');
    titleDiv.className = 'title';
    titleDiv.textContent = path.split('/').pop();
    iconElement.appendChild(titleDiv);

    const extension = isFile ? path.split('.').pop() : '';
    const extData = window.os.registry ? window.os.registry[extension] : null;

    let currentCallback = callback;

    if (extData) {
        const appEmojiSpan = document.createElement('span');
        appEmojiSpan.className = 'app-emoji';
        appEmojiSpan.textContent = extData.emoji;
        iconElement.appendChild(appEmojiSpan);

        currentCallback = function() {
            extData.callback(path);
        };
    }

    iconElement.addEventListener('click', function() {
        currentCallback(path);
    });

    return iconElement;
};
</pre>
