## gui_toolbar_0
### API
<pre style='text-wrap: wrap'>/**
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
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

create function `createToolbar` on the `window.os.gui` object and generate jsdoc that takes one HTMLElement parameter `win`
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from `win` HTML element
- create internal function `addButton` that takes two parameters: text and callback that adds a button to the root DOM element with the text parameter and call the callback when the button is clicked
- return internal addButton function
</pre>
### Output
<pre style='text-wrap: wrap'>window.os = window.os || {};
window.os.gui = window.os.gui || {};

/**
 * Creates a toolbar and appends it to the specified window element.
 * @param {HTMLElement} win - The window element to which the toolbar will be appended.
 * @returns {function(string, function): void} - A function to add buttons to the toolbar.
 */
window.os.gui.createToolbar = function(win) {
    const toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    const placeholder = win.querySelector('.toolbarPlaceholder');
    if (placeholder) {
        placeholder.appendChild(toolbar);
    }

    /**
     * Adds a button to the toolbar.
     * @param {string} text - The text to display on the button.
     * @param {function} callback - The function to call when the button is clicked.
     */
    function addButton(text, callback) {
        const button = document.createElement('button');
        button.textContent = text;
        button.addEventListener('click', callback);
        toolbar.appendChild(button);
    }

    return addButton;
};
</pre>
