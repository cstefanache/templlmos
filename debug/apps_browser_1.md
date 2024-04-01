## apps_browser_1
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

/**
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) { ... }

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
 * Create an icon element for a file or directory at given path
 * @param {string} path - The path to the file or directory
 * @param {function} callback - The callback to call when the icon is clicked
 * @returns {HTMLElement} - The icon element
 */
window.os.getOSIcon = function(path, callback) { ... }

function browser(win, path='') { ... }


 Call register application with 'Browser' title, 📂 as emoji, browser and 450x400 size 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>function browser(win, path='') {
    // Create a container dom element with class `browser`
    let container = document.createElement('div');
    container.className = 'browser';
    
    // Set browserPath to path or `''` if path is undefined or not string
    let browserPath = (typeof path === 'string') ? path : '';
    
    // Generate internal load function that takes path parameter
    let load = (path) => {
        // Set browserPath to path
        browserPath = path;
        
        // Removes all children of the container element
        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }
        
        // If path is not empty, create a new `div` with class icon, inner element `.emoji` with internal span element having content '🔙'  and class `emoji` and on click call load with `path.split('/').slice(0, -1).join('/')`
        if (path !== '') {
            let backButtonDiv = document.createElement('div');
            backButtonDiv.className = 'icon';
            let backButtonSpan = document.createElement('span');
            backButtonSpan.className = 'emoji';
            backButtonSpan.innerText = '🔙';
            backButtonSpan.onclick = () => load(path.split('/').slice(0, -1).join('/'));
            backButtonDiv.appendChild(backButtonSpan);
            container.appendChild(backButtonDiv);
        }
        
        // ls all files in the path and for each item call `getOsIcon` with path+'/'+item and load function as callback
        window.os.fs.ls(path).forEach(item => {
            let iconElement = window.os.getOSIcon(path+'/'+item, () => load(path+'/'+item));
            container.appendChild(iconElement);
        });
    };
    
    // Execute load on browserPath variable
    load(browserPath);
    
    // Create toolbar
    let toolbar = window.os.gui.createToolbar(win);
    
    // Call `addButton` on the toolbar with `📁` text and prompt for a name and call mkdir on current browserPath and provided name
    toolbar('📁', () => {
        let name = prompt('Enter directory name');
        window.os.fs.mkdir(browserPath + '/' + name);
        load(browserPath);
    });
    
    // Call `addButton` on the toolbar with `📄` text and prompt for a name and call write on current browserPath and provided name and '' as content
    toolbar('📄', () => {
        let name = prompt('Enter file name');
        window.os.fs.write(browserPath + '/' + name, '');
        load(browserPath);
    });
    
    // Return dom element 
    return container;
}

window.os.registerApplication('Browser', '📂', browser, 450, 400);

</pre>
