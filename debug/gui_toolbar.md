## gui_toolbar
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Assuming os.gui is already defined as an object
if (typeof window.os === 'undefined') window.os = {};
if (typeof window.os.gui === 'undefined') window.os.gui = {};

// Function to create toolbar
window.os.gui.createToolbar = function(parent) {
    // Create root DOM element with class .toolbar
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append root DOM element to .toolbarPlaceholder from passed parent as parameter
    parent.querySelector('.toolbarPlaceholder').appendChild(toolbar);
    
    // Return an object with addButton function
    return {
        addButton: function(text, callback) {
            // Create button DOM element with text parameter
            var button = document.createElement('button');
            button.textContent = text;
            
            // Append button DOM element to toolbar DOM element
            toolbar.appendChild(button);
            
            // Add event listener to button to call callback when clicked
            button.addEventListener('click', callback);
        }
    };
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript code defines a function `createToolbar` which creates and returns an object with one method `addButton`. The `createToolbar` function takes one parameter `parent` which should be a DOM element. It creates a new `div` element with class `toolbar` and appends it to `.toolbarPlaceholder` inside `parent`. The `addButton` method creates a new `button` element with text content set to `text` parameter and appends it to `toolbar`. It also adds an event listener to `button` which calls `callback` function when `button` is clicked. 

Here's how you can use this function in your code:

```javascript
var toolbarManager = window.os.gui.createToolbar(document.body);  // create toolbar and return its manager
toolbarManager.addButton('Button 1', function() {  // add first button with text "Button 1" and callback function
    console.log('Button 1 clicked');  // this will be logged to console when button is clicked
});
toolbarManager.addButton('Button 2', function() {  // add second button with text "Button 2" and callback function
    console.log('Button 2 clicked');  // this will be logged to console when button is clicked
});
```
In this example, `createToolbar` function creates a toolbar and returns its manager which can be used to add buttons to it. The `addButton` method of `toolbarManager` adds buttons to toolbar with specified text and callback function which will be called when button is clicked. In this case, when "Button 1" or "Button 2" is clicked, corresponding message will be logged to console.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Define a function called `createToolbar` on the `window.os.gui` object that takes one parameter `parent`
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from passed `parent` as parameter
- return an object with the following functions:
  - addButton(text, callback) - add a button to the root DOM element with the text parameter and call the callback when the button is clicked 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is an example of how you can define this function in JavaScript:

```javascript
// Assuming os.gui is already defined as an object
if (typeof window.os === 'undefined') window.os = {};
if (typeof window.os.gui === 'undefined') window.os.gui = {};

// Function to create toolbar
window.os.gui.createToolbar = function(parent) {
    // Create root DOM element with class .toolbar
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append root DOM element to .toolbarPlaceholder from passed parent as parameter
    parent.querySelector('.toolbarPlaceholder').appendChild(toolbar);
    
    // Return an object with addButton function
    return {
        addButton: function(text, callback) {
            // Create button DOM element with text parameter
            var button = document.createElement('button');
            button.textContent = text;
            
            // Append button DOM element to toolbar DOM element
            toolbar.appendChild(button);
            
            // Add event listener to button to call callback when clicked
            button.addEventListener('click', callback);
        }
    };
};

```</pre>
