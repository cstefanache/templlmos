## gui_titleBar
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

window.os.gui.titleBar = function(parentElement, title, close) {
    // Create root DOM element with class .titleBar
    var root = document.createElement('div');
    root.className = 'titleBar';
    
    // Create span containing the title parameter
    var span = document.createElement('span');
    span.textContent = title;
    root.appendChild(span);
    
    // Create button with text '❌' and class 'close'
    var button = document.createElement('button');
    button.textContent = '❌';
    button.className = 'close';
    button.addEventListener('click', close); // Add click event listener to the button
    root.appendChild(button);
    
    // Append root DOM element to parentElement
    parentElement.appendChild(root);
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript function creates a title bar with a title and a close button. The title bar is appended to the parent element provided as an argument to the function. 

Here's how you can use this function in your code:

```javascript
// Get some element to serve as parent for title bar
var parentElement = document.getElementById('myElementId'); 

// Define what should happen when close button is clicked
var closeFunction = function() { 
  // Your code here to handle close event 
}; 

// Call titleBar function to create title bar 
window.os.gui.titleBar(parentElement, 'My Title', closeFunction); 
```
In this example, we first get an element with id 'myElementId' and store it in `parentElement` variable. Then we define `closeFunction` which will be called when close button is clicked. Finally, we call `titleBar` function with `parentElement`, 'My Title' and `closeFunction` as arguments to create title bar with specified title and close event handler. 

Please replace 'My Title' and `closeFunction` with your own values as per your requirements. The `closeFunction` should be defined to handle close event as per your application's logic. 

This function does not return any value, it only creates and appends DOM elements to parent element. If you want to manipulate created elements later, you should store them in variables and use them as needed.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Define a function called `titleBar` object on `window.os.gui` that takes two parameter: parentElement (DOM element), title (string), and a callback `close` and has the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `❌` and class `close` that calls the close callback
- append the root DOM element to parentElement 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is the code in JavaScript to define the `titleBar` function:

```javascript
if (!window.os) {
    window.os = {};
}
if (!window.os.gui) {
    window.os.gui = {};
}

window.os.gui.titleBar = function(parentElement, title, close) {
    // Create root DOM element with class .titleBar
    var root = document.createElement('div');
    root.className = 'titleBar';
    
    // Create span containing the title parameter
    var span = document.createElement('span');
    span.textContent = title;
    root.appendChild(span);
    
    // Create button with text '❌' and class 'close'
    var button = document.createElement('button');
    button.textContent = '❌';
    button.className = 'close';
    button.addEventListener('click', close); // Add click event listener to the button
    root.appendChild(button);
    
    // Append root DOM element to parentElement
    parentElement.appendChild(root);
};

```</pre>
