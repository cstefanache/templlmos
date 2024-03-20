## gui_titleBar
### Instruction: 0
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. `window.os` function is already defined.
### Instruction:
 Define a function called `titleBar` object on `window.os.gui` that takes two parameter: parentElement (DOM element) and title (string) and has the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `❌` that when clicked removes parentElement element from the DOM
- append the root DOM element to parentElement 
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here's how you can define this function in JavaScript:

```javascript
if (!window.os) window.os = {};
if (!window.os.gui) window.os.gui = {};

window.os.gui.titleBar = function(parentElement, title) {
    // Create root DOM element with class .titleBar
    var root = document.createElement('div');
    root.className = 'titleBar';
    
    // Add span containing title to root DOM element
    var span = document.createElement('span');
    span.textContent = title;
    root.appendChild(span);
    
    // Add button with text '❌' to root DOM element
    var button = document.createElement('button');
    button.textContent = '❌';
    button.addEventListener('click', function() {
        // When button is clicked, remove parentElement from DOM
        var parent = parentElement.parentNode;
        if(parent){
            parent.removeChild(parentElement);
        }
    });
    root.appendChild(button);
    
    // Append root DOM element to parentElement
    parentElement.appendChild(root);
};

```</pre>
### Library
<pre style='text-wrap: wrap'>The method signature for the `window.os.gui.titleBar` function is as follows:

```javascript
function titleBar(parentElement, title)

```</pre>
