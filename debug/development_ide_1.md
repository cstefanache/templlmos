## development_ide_1
### API
<pre style='text-wrap: wrap'>function ide(win, path) { ... }
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

/**
 * Compile a source code string into a runnable script.
 * @param {string} source - The source code string to compile.
 */
function compile(source) { ... }


 1. Create an `ide` function that takes a win and path parameter: 
 - create a root dom element with class `ide`
 - create a textarea element with 100% width and 500px height
 - if path is not empty, read the file content and set it to the textarea
 - create toolbar on win
 - add button on the toolbar with `▶️` text and on click execute `compile` function with textarea content
 - add button on the toolbar with `💾` text and on click fs.write textarea content to the path if path is defined, prompt for the path otherwise
 - return dom element
2. Call register application with 'IDE' title, 🧠 as emoji, already defined `ide` function reference and 800x600 size and register for ['script'] extensions 
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

function ide(win, path) {
    // Create root element
    const ideRoot = document.createElement('div');
    ideRoot.className = 'ide';
    
    // Create textarea element
    const textarea = document.createElement('textarea');
    textarea.style.width = '100%';
    textarea.style.height = '500px';
    
    // If path is not empty, read file content and set it to textarea
    if (path) {
        const content = window.os.fs.getFileContentFromPath(path);
        if (content) textarea.value = content;
    }
    
    // Create toolbar on win
    const addButton = window.os.gui.createToolbar(win);
    
    // Add buttons on toolbar
    addButton('▶️', () => compile(textarea.value)); // Execute compile on click
    addButton('💾', () => { // Save on click
        if (path) {
            window.os.fs.write(path, textarea.value);
        } else {
            path = prompt('Please enter a path');
            if (path) window.os.fs.write(path, textarea.value);
        }
    });
    
    // Append textarea to root element
    ideRoot.appendChild(textarea);
    
    // Return root element
    return ideRoot;
}

// Register application with 'IDE' title, 🧠 as emoji, ide function reference and 800x600 size
window.os.registerApplication('IDE', '🧠', ide, 800, 600, ['script']);

</pre>
