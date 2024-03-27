## gui_tests
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 Sure, here is how you can use these functions in your code:

1. `window.os.gui.createWindow` - This is used to create a new window with customizable parameters such as emoji, title, width, and height. The default values are set to '🖥️' for emoji, 'Window' for title, 400 for width, and 300 for height if no arguments are provided. The function returns the root element of the newly created window. 

Example Usage: 
```javascript
var newWindowElement = window.os.gui.createWindow('📚', 'My Book Window', 600, 400);
```

2. `window.os.gui.attachToWindow` - This is used to attach an existing DOM element to an existing window DOM element. The first argument is the window element to which you want to attach the content, and the second argument is the content element you want to attach to the window. 

Example Usage: 
```javascript
var contentElement = document.createElement('p');
contentElement.textContent = "This is some content";
window.os.gui.attachToWindow(newWindowElement, contentElement);
```
In this example, `contentElement` is attached to `newWindowElement`, which is assumed to be an existing window created using `window.os.gui.createWindow`. 

Please note that these functions make use of other helper functions like `bringToFront`, `titleBar`, `makeDraggable`, and `makeResizable`, which you would need to define as well to make these examples work. These helper functions handle the specific behaviors of creating and managing windows, such as making elements draggable, resizable, and bringing elements to front of other elements in the DOM. 

Also, these examples assume you have already included these JavaScript files in your HTML file, and they have been loaded before these examples are run. If not, you would need to include them in your HTML file using `<script>` tags. 

Remember to replace `'📚'`, `'My Book Window'`, `600`, `400`, and `"This is some content"` with your desired values to customize your new window and its content.

```

 create an element h1 with text `hello world!` and attach to a window with title `Hello World` and emoji `🌍` having 300x200 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here's an example of how to create an h1 element with text "hello world!" and attach it to a window with title "Hello World" and emoji "🌍" having 300x200 size using the provided functions:

```javascript
// Create new window with emoji '🌍', title 'Hello World', width 300, height 200
var newWindowElement = window.os.gui.createWindow('🌍', 'Hello World', 300, 200);

// Create new h1 element with text 'hello world!'
var h1Element = document.createElement('h1');
h1Element.textContent = "hello world!";

// Attach h1 element to new window
window.os.gui.attachToWindow(newWindowElement, h1Element);

```</pre>
