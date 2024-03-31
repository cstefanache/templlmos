## osbase_fs-tests_0
### API
<pre style='text-wrap: wrap'></pre>
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



 create a new directory in the root directory called `fstest`
create a new file in the `fstest` directory called `test.txt` with the content `hello world`
list the entries in the `fstest` directory and log it to console
read the content of the `fstest/test.txt` file and log it to console
remove the `fstest` directory 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create a new directory in the root directory called `fstest`
window.os.fs.mkdir('fstest');

// Create a new file in the `fstest` directory called `test.txt` with the content `hello world`
window.os.fs.write('fstest/test.txt', 'hello world');

// List the entries in the `fstest` directory and log it to console
console.log(window.os.fs.ls('fstest'));

// Read the content of the `fstest/test.txt` file and log it to console
console.log(window.os.fs.getFileContentFromPath('fstest/test.txt'));

// Remove the `fstest` directory 
window.os.fs.rm('fstest');

</pre>
