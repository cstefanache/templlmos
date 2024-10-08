## gui_titleBar_0
### API
<pre style='text-wrap: wrap'>/**
 * Creates a title bar with a title and a close button.
 * @param {HTMLElement} parentElement - The DOM element to append this title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {function} close - The callback to call when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 Define a function `titleBar` on the `window.os.gui` object that takes two parameter: parentElement (DOM element), title (string), and a callback `close` and has the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `❌` and class `close` that calls the close callback
- append the root DOM element to parentElement 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Assuming window.os is an existing object with gui as its property
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

/**
 * Creates a title bar with a title and a close button.
 * @param {HTMLElement} parentElement - The DOM element to append this title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {function} close - The callback to call when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) {
    // Create root element
    var root = document.createElement('div');
    root.classList.add('titleBar');
    
    // Create title span
    var titleSpan = document.createElement('span');
    titleSpan.textContent = title;
    root.appendChild(titleSpan);
    
    // Create close button
    var closeButton = document.createElement('button');
    closeButton.textContent = '❌';
    closeButton.classList.add('close');
    closeButton.addEventListener('click', close); // Add click event listener to close button
    root.appendChild(closeButton);
    
    // Append root to parent element
    parentElement.appendChild(root);
};

</pre>
