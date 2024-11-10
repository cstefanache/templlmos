## gui_tests_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.

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
 * Creates a toolbar and appends it to the specified window element.
 * @param {HTMLElement} win - The window element to which the toolbar will be appended.
 * @returns {function(string, function): void} - A function to add buttons to the toolbar.
 */
window.os.gui.createToolbar = function(win) { ... }
    /**
     * Adds a button to the toolbar.
     * @param {string} text - The text to display on the button.
     * @param {function} callback - The function to call when the button is clicked.
     */



create an element h1 with text `hello world!` and attach to a window with title `Hello World` and emoji `🌍` having 300x200 size
create an element h1 with text `good bye world!` and attach to a window with title `Good Bye` and emoji `👋` having 300x200 size
</pre>
### Output
<pre style='text-wrap: wrap'>// Create the first window and attach the first h1 element
const helloWorldWindow = window.os.gui.createWindow('🌍', 'Hello World', 300, 200);
const helloWorldH1 = document.createElement('h1');
helloWorldH1.textContent = 'hello world!';
window.os.gui.attachToWindow(helloWorldWindow, helloWorldH1);

// Create the second window and attach the second h1 element
const goodByeWorldWindow = window.os.gui.createWindow('👋', 'Good Bye', 300, 200);
const goodByeWorldH1 = document.createElement('h1');
goodByeWorldH1.textContent = 'good bye world!';
window.os.gui.attachToWindow(goodByeWorldWindow, goodByeWorldH1);
</pre>
