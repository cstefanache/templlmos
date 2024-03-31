## gui_tests_0
### API
<pre style='text-wrap: wrap'></pre>
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
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) { ... }



 create an element h1 with text `hello world!` and attach to a window with title `Hello World` and emoji `🌍` having 300x200 size
create an element h1 with text `good bye world!` and attach to a window with title `Good Bye` and emoji `👋` having 300x200 size 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// create h1 element
let h1_1 = document.createElement("h1");
h1_1.textContent = "Hello World!";

let h1_2 = document.createElement("h1");
h1_2.textContent = "Good Bye World!";

// create windows
let win1 = window.os.gui.createWindow("🌍", "Hello World", 300, 200);
let win2 = window.os.gui.createWindow("👋", "Good Bye", 300, 200);

// attach h1 elements to windows
window.os.gui.attachToWindow(win1, h1_1);
window.os.gui.attachToWindow(win2, h1_2);

</pre>
