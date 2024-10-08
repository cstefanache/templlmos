## registry_hello-world_0
### API
<pre style='text-wrap: wrap'>/**
 * Create a root element div having an h1 child element with 'Hello World' text
 * If path is defined append a pre element containing the content of reading the file at the path
 * @param {HTMLElement} parent - The parent element to append the created elements to
 * @param {string} [path] - The path to a file to read its content from
 * @returns {HTMLElement} - The root element containing h1 and pre elements
 */
function helloWorld(parent, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
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



 Create a `helloWorld` function that takes a parent and path parameter:
 - creates and returns a root element `div` having an h1 child element with 'Hello World' text
 - if path is defined append a pre element containing the content of reading the file at the path
 - returns the root element
after definition, register application with 'hello world' title, 👋 as emoji, `helloWorld` function and 300x200 size 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Create a root element div having an h1 child element with 'Hello World' text
 * If path is defined append a pre element containing the content of reading the file at the path
 * @param {HTMLElement} parent - The parent element to append the created elements to
 * @param {string} [path] - The path to a file to read its content from
 * @returns {HTMLElement} - The root element containing h1 and pre elements
 */
function helloWorld(parent, path) {
    // Create root div element
    const root = document.createElement('div');
    
    // Create h1 element with 'Hello World' text
    const h1 = document.createElement('h1');
    h1.textContent = 'Hello World';
    root.appendChild(h1);
    
    // If path is provided, create pre element with file content
    if (path) {
        const pre = document.createElement('pre');
        pre.textContent = window.os.fs.getFileContentFromPath(path);
        root.appendChild(pre);
    }
    
    // Append root element to parent
    parent.appendChild(root);
    
    return root;
}

// Register application with 'hello world' title, 👋 as emoji, helloWorld function and 300x200 size
window.os.registerApplication('hello world', '👋', helloWorld, 300, 200);

</pre>
