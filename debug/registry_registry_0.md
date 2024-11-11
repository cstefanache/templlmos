## registry_registry_0
### API
<pre style='text-wrap: wrap'>/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to be displayed for the application.
 * @param {Function} callback - The function to be called when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>create a new function `registerApplication` on the `window.os` object and jsdoc that takes a title, emoji, callback, width=400 and height = 400 and a an array of extensions being undefined by default having the following functionality:
- define an internal `execute` that takes a spread params:
  - creates a new window instance with the title, emoji, width and height and saves it to a constant
  - call attach to window the result of calling the callback with the window instance and spread params
- if extensions is defined, call `registerExtension` for each extension with extension, emoji and the execute function
- call addApp with the emoji, title and callback that calls the execute function with no parameters</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to be displayed for the application.
 * @param {Function} callback - The function to be called when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) {
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
