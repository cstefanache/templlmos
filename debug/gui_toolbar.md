## gui_toolbar
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Assuming os.gui is already defined as an object
if (typeof window.os === 'undefined') window.os = {};
if (typeof window.os.gui === 'undefined') window.os.gui = {};

// Function to create toolbar
window.os.gui.createToolbar = function(win) {
    // Create root DOM element with class .toolbar
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append root DOM element to .toolbarPlaceholder from win parameter
    win.querySelector('.toolbarPlaceholder').appendChild(toolbar);
    
    // Return an object with addButton function
    return {
        addButton: function(text, callback) {
            // Create button element
            var button = document.createElement('button');
            button.textContent = text;
            
            // Add click event listener to button
            button.addEventListener('click', callback);
            
            // Append button to toolbar
            toolbar.appendChild(button);
        }
    };
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript function creates a toolbar with buttons and attaches them to a specified HTML element. The toolbar and buttons are created using DOM manipulation methods provided by JavaScript. The function returns an object with a method `addButton`, which allows you to add buttons to the toolbar with custom text and click event callbacks. 

Here's how you can use this function in your code:

```javascript
// Assume you have a reference to your window or iframe here
var myWindow = ...; 

// Create toolbar instance
var toolbarInstance = os.gui.createToolbar(myWindow); 

// Add buttons to toolbar
toolbarInstance.addButton('Button 1', function() {
    console.log('Button 1 clicked');
});
toolbarInstance.addButton('Button 2', function() {
    console.log('Button 2 clicked');
});
toolbarInstance.addButton('Button 3', function() {
    console.log('Button 3 clicked');
});
```
In this example, we first create a toolbar instance using `os.gui.createToolbar` and pass in our target window or iframe reference `myWindow`. Then we add three buttons to the toolbar with custom text and click event callbacks. The callbacks will be executed when their respective buttons are clicked, and will log a message to the console indicating which button was clicked. 

Please replace `myWindow` with your actual reference to your HTML element where you want to add the toolbar.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Define a function called `createToolbar` on the `window.os.gui` object that takes one parameter `win`
- create a root DOM element with the class `.toolbar`
- append the root DOM element to the `.toolbarPlaceholder` from `win` parameter
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
window.os.gui.createToolbar = function(win) {
    // Create root DOM element with class .toolbar
    var toolbar = document.createElement('div');
    toolbar.className = 'toolbar';
    
    // Append root DOM element to .toolbarPlaceholder from win parameter
    win.querySelector('.toolbarPlaceholder').appendChild(toolbar);
    
    // Return an object with addButton function
    return {
        addButton: function(text, callback) {
            // Create button element
            var button = document.createElement('button');
            button.textContent = text;
            
            // Add click event listener to button
            button.addEventListener('click', callback);
            
            // Append button to toolbar
            toolbar.appendChild(button);
        }
    };
};

```</pre>
