## development_ide_0
### API
<pre style='text-wrap: wrap'>/**
 * Compile a source code string into a runnable script.
 * @param {string} source - The source code string to compile.
 */
function compile(source) { ... }
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
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) { ... }



 Create `compile` function that takes a source parameter and:
 - remove the script tag with id `run-script` if exists
 - fetch post  to `http://localhost:8080` with a json having {instruction: source}, and on response create a script tag with id `run-script` and add the response text content to the script tag
 - add end function comment 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Compile a source code string into a runnable script.
 * @param {string} source - The source code string to compile.
 */
function compile(source) {
    // Remove existing script tag with id 'run-script' if exists
    var existingScriptTag = document.getElementById('run-script');
    if (existingScriptTag) {
        existingScriptTag.parentNode.removeChild(existingScriptTag);
    }
    
    // Fetch POST request with source code as JSON data
    fetch('http://localhost:8080', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({instruction: source})
    })
    .then(response => response.text()) // Get response text content
    .then(data => {
        // Create a new script tag with id 'run-script' and add response text content to it
        var newScriptTag = document.createElement('script');
        newScriptTag.id = 'run-script';
        newScriptTag.textContent = data;
        document.body.appendChild(newScriptTag);
    })
    .catch(error => console.error('Error:', error)); // Handle any errors that occurred during fetch request
}

</pre>
