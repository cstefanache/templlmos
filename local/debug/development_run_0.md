## development_run_0
### API
<pre style='text-wrap: wrap'>/**
 * Run an application in a new window.
 * @param {function} callback - The callback to run in the new window.
 * @param {number} [width=500] - The width of the window in pixels.
 * @param {number} [height=400] - The height of the window in pixels.
 */
window.os.runApp = function(callback, width = 500, height = 400) { ... }
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



 create a new function `window.os.runApp` object that takes a callback, width and height defaulting to 500 and 400, having the following functionality:
  - creates a new window instance with the `Development` title , 🔥 emoji, width and height and saves it to a constant
  - attach to window the result of calling the callback with the window instance 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Run an application in a new window.
 * @param {function} callback - The callback to run in the new window.
 * @param {number} [width=500] - The width of the window in pixels.
 * @param {number} [height=400] - The height of the window in pixels.
 */
window.os.runApp = function(callback, width = 500, height = 400) {
    // Create a new window instance
    const appWindow = window.os.gui.createWindow('🔥', 'Development', width, height);
    
    // Attach content to the window
    const contentElement = callback(appWindow);
    window.os.gui.attachToWindow(appWindow, contentElement);
};

</pre>
