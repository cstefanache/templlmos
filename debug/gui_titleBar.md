## gui_titleBar
### API
<pre style='text-wrap: wrap'>The provided code defines a JavaScript function named `titleBar` under the namespace `window.os.gui`. The function creates a title bar element with a title, a close button, and appends it to a parent element. Here are the method signatures for this function:

```javascript
/**
 * Creates a title bar element with a title, a close button, and appends it to a parent element.
 * @param {HTMLElement} parentElement - The parent element to append the title bar to.
 * @param {string} title - The title to display in the title bar.
 * @param {function} close - The callback function to execute when the close button is clicked.
 */
window.os.gui.titleBar = function(parentElement, title, close) { ... };

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. `window.os` function is already defined.
### Instruction:
 Define a function called `titleBar` object on `window.os.gui` that takes two parameter: parentElement (DOM element), title (string), and a callback `close` and has the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `❌` and class `close` that calls the close callback
- append the root DOM element to parentElement 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here's how you can define this function in JavaScript:

```javascript
if (!window.os) window.os = {};
if (!window.os.gui) window.os.gui = {};

window.os.gui.titleBar = function(parentElement, title, close) {
    // Create root DOM element with class .titleBar
    var root = document.createElement('div');
    root.className = 'titleBar';
    
    // Add span containing title to root DOM element
    var span = document.createElement('span');
    span.textContent = title;
    root.appendChild(span);
    
    // Add button with text '❌' and class 'close' to root DOM element
    var button = document.createElement('button');
    button.textContent = '❌';
    button.className = 'close';
    button.addEventListener('click', close); // Add event listener for close callback
    root.appendChild(button);
    
    // Append root DOM element to parentElement
    parentElement.appendChild(root);
};

```</pre>
