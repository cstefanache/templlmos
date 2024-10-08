## gui_toolbar_0
### API
<pre style='text-wrap: wrap'>/**
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 create function `createToolbar` on the `window.os.gui` object and generate jsdoc that takes one HTMLElement parameter `win`
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from `win` HTML element
- create internal function `addButton` that takes two parameters: text and callback that adds a button to the root DOM element with the text parameter and call the callback when the button is clicked
- return internal addButton function 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Create a toolbar with a button inside it.
 * @param {HTMLElement} win - The window element to add toolbar to.
 * @returns {function(string, function): void} - The addButton function.
 */
window.os.gui.createToolbar = function(win) {
    // Create a root DOM element with class .toolbar
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append the root DOM element to .toolbarPlaceholder from win HTML element
    win.querySelector('.toolbarPlaceholder').appendChild(toolbar);
    
    /**
     * Add a button to the toolbar with a specific text and callback when clicked.
     * @param {string} text - The text to display on the button.
     * @param {function} callback - The callback to call when the button is clicked.
     */
    var addButton = function(text, callback) {
        // Create a button element with text parameter
        var button = document.createElement('button');
        button.textContent = text;
        
        // Add event listener to call callback when button is clicked
        button.addEventListener('click', callback);
        
        // Append button to toolbar root element
        toolbar.appendChild(button);
    };
    
    // Return addButton function
    return addButton;
};

</pre>
