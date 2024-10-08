## registry_app-icon_0
### API
<pre style='text-wrap: wrap'>/**
 * Create an icon element for a file or directory at given path
 * @param {string} path - The path to the file or directory
 * @param {function} callback - The callback to call when the icon is clicked
 * @returns {HTMLElement} - The icon element
 */
window.os.getOSIcon = function(path, callback) { ... }
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
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Create an icon element for a file or directory at given path
 * @param {string} path - The path to the file or directory
 * @param {function} callback - The callback to call when the icon is clicked
 * @returns {HTMLElement} - The icon element
 */
window.os.getOSIcon = function(path, callback) {
    const isFile = window.os.fs.isFile(path);
    const rootElement = document.createElement('div');
    rootElement.classList.add('icon');
    
    const emojiElement = document.createElement('span');
    emojiElement.classList.add('emoji');
    emojiElement.textContent = isFile ? '📄' : '📁';
    rootElement.appendChild(emojiElement);
    
    const titleElement = document.createElement('div');
    titleElement.classList.add('title');
    titleElement.textContent = path.split('/').pop(); // Assuming path is a Unix-like path
    rootElement.appendChild(titleElement);
    
    const ext = path.split('.').pop(); // Assuming path has an extension
    const extData = window.os.registry[ext];
    if (extData) {
        const appEmojiElement = document.createElement('span');
        appEmojiElement.classList.add('app-emoji');
        appEmojiElement.textContent = extData.emoji;
        rootElement.appendChild(appEmojiElement);
        
        let currentCallback = path => extData.callback(path); // Closure for path
        rootElement.addEventListener('click', () => currentCallback(path));
    } else {
        let currentCallback = path => callback(path); // Closure for path
        rootElement.addEventListener('click', () => currentCallback(path));
    }
    
    return rootElement;
};

</pre>
