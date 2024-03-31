## osbase_filesystem_0
### API
<pre style='text-wrap: wrap'>/**
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
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 Load the `filesystem` object from the local storage as json
Define the `window.os.fs` object and define the following functions on it (remove leading and trailing `/` from the path):
- `window.os.fs.sync` function that save the `filesystem` object to the local storage.
- `window.os.fs.getFileContentFromPath` function that returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object and return the value at path (allow undefined or empty string). if the path starts with `/` remove the leading `/`
- `window.os.fs.write` function that writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
- `window.os.fs.ls` function that returns a list of entries in the `filesystem` object at the given path. if path is empty or not found, return the root entries.
- `window.os.fs.mkdir` function that creates a new directory in the `filesystem` object at the given path and directory name. in the end execute the `sync` method.
- `window.os.fs.rm` function that removes the object at the given path and file name. in the end execute the `sync` method.
- `window.os.fs.isFile` function that returns true the entry at the given path is a string. 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Load the filesystem object from localStorage
let filesystem = JSON.parse(localStorage.getItem('filesystem')) || {};

// Define window.os.fs
if (!window.os) {
    window.os = {};
}
if (!window.os.fs) {
    window.os.fs = {};
}

/**
 * Save the filesystem object to localStorage
 */
window.os.fs.sync = function() {
    localStorage.setItem('filesystem', JSON.stringify(filesystem));
}

/**
 * Get file content at given path
 * @param {string} path - The path to the file
 * @returns {string|undefined} - The content of the file or undefined if not found
 */
window.os.fs.getFileContentFromPath = function(path) {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    for (let dir of path) {
        if (!current[dir]) {
            return undefined;
        }
        current = current[dir];
    }
    return typeof current === 'string' ? current : undefined;
}

/**
 * Write content to a file at given path
 * @param {string} path - The path to the file
 * @param {string} content - The content to write to the file
 */
window.os.fs.write = function(path, content) {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    for (let dir of path.slice(0, -1)) {
        if (!current[dir]) {
            current[dir] = {};
        }
        current = current[dir];
    }
    current[path[path.length - 1]] = content;
    this.sync();
}

/**
 * List entries at given path
 * @param {string} path - The path to list entries at
 * @returns {Array} - An array of entries at the path or root if path is not found
 */
window.os.fs.ls = function(path = '') {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    for (let dir of path) {
        if (!current[dir]) {
            return Object.keys(filesystem);
        }
        current = current[dir];
    }
    return Object.keys(current);
}

/**
 * Create a directory at given path
 * @param {string} path - The path to create a directory at
 */
window.os.fs.mkdir = function(path) {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    for (let dir of path) {
        if (!current[dir]) {
            current[dir] = {};
        }
        current = current[dir];
    }
    this.sync();
}

/**
 * Remove a file or directory at given path
 * @param {string} path - The path to remove at
 */
window.os.fs.rm = function(path) {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    let parent = filesystem;
    for (let dir of path.slice(0, -1)) {
        if (!current[dir]) {
            return; // Path not found
        }
        parent = current;
        current = current[dir];
    }
    delete parent[path[path.length - 1]];
    this.sync();
}

/**
 * Check if a path is a file
 * @param {string} path - The path to check
 * @returns {boolean} - True if path is a file, false otherwise
 */
window.os.fs.isFile = function(path) {
    path = path.replace(/^\/|\/$/g, '').split('/');
    let current = filesystem;
    for (let dir of path) {
        if (!current[dir]) {
            return false; // Path not found or not a file
        }
        current = current[dir];
    }
    return typeof current === 'string'; // Check if current is a string (file)
}

</pre>
