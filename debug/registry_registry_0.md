## registry_registry_0
### API
<pre style='text-wrap: wrap'>/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to display for the application.
 * @param {Function} callback - The function to call when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions=undefined] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions = undefined) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Given the following implemented functions:
/**
 * Creates a new window with a title, emoji, and specified dimensions.
 * @param {string} emoji - The emoji to display in the title.
 * @param {string} title - The title of the window.
 * @param {number} [width=400] - The width of the window.
 * @param {number} [height=300] - The height of the window.
 * @returns {HTMLElement} The created window element.
 */
window.os.gui.createWindow = function(emoji, title, width = 400, height = 300) { ... }
/**
 * Attaches a content element to the content placeholder of a window element.
 * @param {HTMLElement} windowElement - The window element to which the content will be attached.
 * @param {HTMLElement} contentElement - The content element to be appended to the window's content placeholder.
 */
window.os.gui.attachToWindow = function(windowElement, contentElement) { ... }

/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to display in the icon.
 * @param {string} title - The title to display in the icon.
 * @param {Function} callback - The function to call when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }

/**
 * Creates an OS icon element for a given path and sets up a callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The callback function to be executed on click.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) { ... }
currentCallback = function() { ... }



create a new function `registerApplication` on the `window.os` object and jsdoc that takes a title, emoji, callback, width=400 and height = 400 and a an array of extensions being undefined by default having the following functionality:
- define an internal `execute` that takes a spread params:
  - creates a new window instance with the title, emoji, width and height and saves it to a constant
  - attach to window the result of calling the callback with the window instance and spread params
- if extensions is defined, call `registerExtension` for each extension with extension, emoji and the execute function
- call addApp with the emoji, title and callback that calls the execute function with no parameters
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to display for the application.
 * @param {Function} callback - The function to call when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions=undefined] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions = undefined) {
    const execute = (...params) => {
        const windowInstance = window.os.gui.createWindow(emoji, title, width, height);
        window.os.gui.attachToWindow(windowInstance, callback(windowInstance, ...params));
    };

    if (extensions) {
        extensions.forEach(extension => {
            window.os.registerExtension(extension, emoji, execute);
        });
    }

    window.os.addApp(emoji, title, () => execute());
};
</pre>
