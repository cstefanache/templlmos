## gui_tests_1
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



 create a h3 element with the text 'here
create a window with title `Toolbar` and emoji `🛠`
create a toolbar on window and add button with text `👋` that alerts `clicked` on callback
attach the h3 element to the window 
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

// create h3 element
let h3 = document.createElement("h3");
h3.textContent = "Here";

// create window
let win = window.os.gui.createWindow("🛠", "Toolbar");

// create toolbar on window
let addButton = window.os.gui.createToolbar(win);
addButton("👋", () => alert("clicked"));  // add button to toolbar

// attach h3 element to window
window.os.gui.attachToWindow(win, h3);

</pre>
