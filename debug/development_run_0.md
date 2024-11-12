## development_run_0
### API

<pre style='text-wrap: wrap'>
/**
 * Runs an application by creating a new window and attaching content to it.
 * @param {Function} callback - A function that returns an HTMLElement to be attached to the window.
 * @param {number} [width=500] - The width of the window.
 * @param {number} [height=400] - The height of the window.
 */
window.os.runApp = function(callback, width = 500, height = 400) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
create a new function `window.os.runApp` object that takes a callback, width and height defaulting to 500 and 400, having the following functionality:
  - creates a new window instance with the `Development` title , 🔥 emoji, width and height and saves it to a constant
  - attach to window the result of calling the callback with the window instance
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Runs an application by creating a new window and attaching content to it.
 * @param {Function} callback - A function that returns an HTMLElement to be attached to the window.
 * @param {number} [width=500] - The width of the window.
 * @param {number} [height=400] - The height of the window.
 */
window.os.runApp = function(callback, width = 500, height = 400) {
    const windowInstance = window.os.gui.createWindow('🔥', 'Development', width, height);
    const content = callback(windowInstance);
    window.os.gui.attachToWindow(windowInstance, content);
};

</pre>
