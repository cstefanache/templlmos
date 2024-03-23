## gui_toolbar
### API
<pre style='text-wrap: wrap'>The function signatures are as follows:

1. `createToolbar(parent): Object` - This function creates a toolbar in a given parent element and returns an object that has a function to add buttons to the toolbar. The parent parameter should be a DOM element where the toolbar will be appended to.
2. `addButton(text, callback): undefined` - This function adds a button to the toolbar created by `createToolbar()` function. The text parameter should be a string that will be set as the button's text content, and the callback parameter should be a function that will be called when the button is clicked. The function does not return anything, so it returns undefined.

Here's how you can use these methods:

```javascript
var toolbar = window.os.gui.createToolbar(document.body);
toolbar.addButton('Button 1', function() { console.log('Button 1 clicked'); });
toolbar.addButton('Button 2', function() { console.log('Button 2 clicked'); });

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 Define a function called `createToolbar` on the `window.os.gui` object that takes one parameter `parent`
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from passed `parent` as parameter
- return an object with the following functions:
  - addButton(text, callback) - add a button to the root DOM element with the text parameter and call the callback when the button is clicked 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can define this function in JavaScript:

```javascript
// Assuming window.os is already defined as an object
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

// Function to create toolbar
window.os.gui.createToolbar = function(parent) {
    // Create root DOM element
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append to parent's .toolbarPlaceholder
    var toolbarPlaceholder = parent.querySelector('.toolbarPlaceholder');
    toolbarPlaceholder.appendChild(toolbar);
    
    // Return object with addButton function
    return {
        addButton: function(text, callback) {
            // Create button DOM element
            var button = document.createElement('button');
            button.textContent = text;
            
            // Append to toolbar
            toolbar.appendChild(button);
            
            // Add click event listener to call callback
            button.addEventListener('click', callback);
        }
    };
};

```</pre>
