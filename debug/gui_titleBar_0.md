## gui_titleBar_0
### API

<pre style='text-wrap: wrap'>
/**
 * Creates a title bar with a title and a close button.
 * @param {HTMLElement} parentElement - The parent DOM element to append the title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {Function} close - The callback function to call when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Define a function `titleBar` on the `window.os.gui` object that takes two parameter: parentElement (DOM element), title (string), and a callback `close` and has the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `❌` and class `close` that calls the close callback
- append the root DOM element to parentElement
</pre>
### Output

<pre style='text-wrap: wrap'>
window.os = window.os || {};
window.os.gui = window.os.gui || {};

/**
 * Creates a title bar with a title and a close button.
 * @param {HTMLElement} parentElement - The parent DOM element to append the title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {Function} close - The callback function to call when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) {
    var titleBar = document.createElement('div');
    titleBar.className = 'titleBar';

    var titleSpan = document.createElement('span');
    titleSpan.textContent = title;
    titleBar.appendChild(titleSpan);

    var closeButton = document.createElement('button');
    closeButton.textContent = '❌';
    closeButton.className = 'close';
    closeButton.onclick = close;
    titleBar.appendChild(closeButton);

    parentElement.appendChild(titleBar);
};

</pre>
