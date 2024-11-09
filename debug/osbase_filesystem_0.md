## osbase_filesystem_0
### API
<pre style='text-wrap: wrap'>/**
 * Processes and returns a path by taking into account '..', '//' and '/'.
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
 * @param {string} path - The path where to create the object.
 */
window.os.fs.mkdir = function(path) { ... }
/**
 * Removes the object at the given path.
 * @param {string} path - The path of the object to remove.
 */
window.os.fs.rm = function(path) { ... }
/**
 * Writes the content to an entry in the filesystem object at the given path.
 * @param {string} path - The path where to write the content.
 * @param {string} content - The content to write.
 */
window.os.fs.write = function(path, content) { ... }
/**
 * Reads an entry split by '\n' in the filesystem object at the given path.
 * @param {string} path - The path of the file to read.
 * @returns {Array|null} - An array of lines or null if not found.
 */
window.os.fs.read = function(path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Load the `filesystem` object from the local storage as json, if it does not exist create an empty object with a property `about.txt` with the content `Welcome to TempLLMOS`
Define the following functions on the window.os.fs object:
 `getPath` - process and return a path by taking into account `..`, `//` and `/`. return null if the path is invalid
 `isValidPath` - checks if the path is valid
 `ls` - returns a list of entries in the filesystem object at the given path
 `mkdir` - creates an empty object at the given path
 `rm` - removes the object at the given path
 `write` - writes the content to an entry in the filesystem object at the given path
 `read` - reads an entry split by `
` in the filesystem object at the given path, last element in path is the file name
</pre>
### Output
<pre style='text-wrap: wrap'>// Load the filesystem object from local storage or create a default one
const filesystem = JSON.parse(localStorage.getItem('filesystem')) || {
    'about.txt': 'Welcome to TempLLMOS'
};
localStorage.setItem('filesystem', JSON.stringify(filesystem));

// Define the os.fs object
window.os = window.os || {};
window.os.fs = {};

/**
 * Processes and returns a path by taking into account '..', '//' and '/'.
 * @param {string} path - The path to process.
 * @returns {string|null} - The processed path or null if invalid.
 */
window.os.fs.getPath = function(path) {
    const parts = path.split('/').filter(part => part !== '' && part !== '.');
    const stack = [];
    for (const part of parts) {
        if (part === '..') {
            if (stack.length > 0) {
                stack.pop();
            } else {
                return null;
            }
        } else {
            stack.push(part);
        }
    }
    return '/' + stack.join('/');
};

/**
 * Checks if the path is valid.
 * @param {string} path - The path to check.
 * @returns {boolean} - True if valid, false otherwise.
 */
window.os.fs.isValidPath = function(path) {
    return typeof path === 'string' && path.startsWith('/') && !path.includes('//');
};

/**
 * Returns a list of entries in the filesystem object at the given path.
 * @param {string} path - The path to list entries from.
 * @returns {Array} - An array of entries.
 */
window.os.fs.ls = function(path) {
    const currentDir = filesystem;
    const parts = path.split('/').filter(part => part !== '');
    for (const part of parts) {
        if (currentDir[part]) {
            currentDir = currentDir[part];
        } else {
            return [];
        }
    }
    return Object.keys(currentDir);
};

/**
 * Creates an empty object at the given path.
 * @param {string} path - The path where to create the object.
 */
window.os.fs.mkdir = function(path) {
    const parts = path.split('/').filter(part => part !== '');
    let currentDir = filesystem;
    for (const part of parts) {
        if (!currentDir[part]) {
            currentDir[part] = {};
        }
        currentDir = currentDir[part];
    }
};

/**
 * Removes the object at the given path.
 * @param {string} path - The path of the object to remove.
 */
window.os.fs.rm = function(path) {
    const parts = path.split('/').filter(part => part !== '');
    let currentDir = filesystem;
    for (let i = 0; i < parts.length - 1; i++) {
        if (currentDir[parts[i]]) {
            currentDir = currentDir[parts[i]];
        } else {
            return;
        }
    }
    delete currentDir[parts[parts.length - 1]];
};

/**
 * Writes the content to an entry in the filesystem object at the given path.
 * @param {string} path - The path where to write the content.
 * @param {string} content - The content to write.
 */
window.os.fs.write = function(path, content) {
    const parts = path.split('/').filter(part => part !== '');
    let currentDir = filesystem;
    for (let i = 0; i < parts.length - 1; i++) {
        if (!currentDir[parts[i]]) {
            currentDir[parts[i]] = {};
        }
        currentDir = currentDir[parts[i]];
    }
    currentDir[parts[parts.length - 1]] = content;
};

/**
 * Reads an entry split by '\n' in the filesystem object at the given path.
 * @param {string} path - The path of the file to read.
 * @returns {Array|null} - An array of lines or null if not found.
 */
window.os.fs.read = function(path) {
    const parts = path.split('/').filter(part => part !== '');
    let currentDir = filesystem;
    for (const part of parts) {
        if (currentDir[part]) {
            currentDir = currentDir[part];
        } else {
            return null;
        }
    }
    return currentDir.split('\n');
};
</pre>
