## registry_registry_0
### API
<pre style='text-wrap: wrap'>/**
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
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
* Create a new window with given emoji, title, width and height.
* @param {string} emoji - The emoji to display in the window's title bar.
* @param {string} title - The title to display in the window's title bar.
* @param {number} [width=400] - The width of the window in pixels.
* @param {number} [height=300] - The height of the window in pixels.
* @return {HTMLElement} The root DOM element of the newly created window.
*/
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) { ... }
/**
* Attach content to an existing window.
* @param {HTMLElement} windowElement - The window to attach content to.
* @param {HTMLElement} contentElement - The content to attach to the window.
*/
window.os.gui.attachToWindow = function(windowElement, contentElement) { ... }

/**
 * Adds an application to the desktop content.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }

/**
 * Create an icon element for a file or directory at given path
 * @param {string} path - The path to the file or directory
 * @param {function} callback - The callback to call when the icon is clicked
 * @returns {HTMLElement} - The icon element
 */
window.os.getOSIcon = function(path, callback) { ... }



 create a new function `registerApplication` on the `window.os` object and jsdoc that takes a title, emoji, callback, width=400 and height = 400 and a an array of extensions being undefined by default having the following functionality:
- define an internal `execute` that takes a spread params:
  - creates a new window instance with the title, emoji, width and height and saves it to a constant
  - attach to window the result of calling the callback with the window instance and spread params
- if extensions is defined, call `registerExtension` for each extension with extension, emoji and the execute function
- call addApp with the emoji, title and callback that calls the execute function with no parameters 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Register an application on the desktop.
 * 
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 * @param {number} [width=400] - The width of the application's window in pixels.
 * @param {number} [height=400] - The height of the application's window in pixels.
 * @param {Array<string>} [extensions] - The file extensions to register for this application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) {
    const execute = (...params) => {
        const windowInstance = window.os.gui.createWindow(emoji, title, width, height);
        window.os.gui.attachToWindow(windowInstance, callback(windowInstance, ...params));
    };
    
    if (extensions) {
        extensions.forEach(extension => {
            // Assuming `registerExtension` is also available on `window.os` object
            // and it takes an extension, emoji and callback as parameters
            window.os.registerExtension(extension, emoji, execute);
        });
    }
    
    // Add application to desktop
    window.os.addApp(emoji, title, () => execute());
};

</pre>
