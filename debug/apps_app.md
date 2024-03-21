## apps_app
### Instruction: 0
<pre style='text-wrap: wrap'>Sure, here's a simple usage of the `window.os.gui.createWindow` function in a JavaScript file:

```javascript
// First, make sure the necessary functions are defined in the os.gui object
// This is done in the previous code snippet, so we assume it's been done here
// ...

// Then, you can create a new window with a specific emoji, title, content, width, and height like this:
const contentElement = document.createElement('p');
contentElement.textContent = 'Hello, World 🌍';
window.os.gui.createWindow('🖥️', 'My First Window', contentElement, 600, 400);

```The method signature for the `window.os.desktop.addApp` function is as follows:

```javascript
function addApp(emoji: string, title: string, callback: Function): void;

``` Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 create a new function `application` on the `window.os` object that takes a title, emoji, callback, width=400 and height = 400:
create an internal `initialize` function that creates a new window with the title, emoji, width and height and add child the element returned by executing of the callback passed as parameter
call addApp with the emoji, title and initialize function 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here's how you can create this new `application` function on the `window.os` object:

```javascript
window.os = window.os || {};

window.os.application = function(title, emoji, callback, width=400, height=400) {
    // Create an internal initialize function that creates a new window with the title, emoji, width and height and add child the element returned by executing of the callback passed as parameter
    const initialize = () => {
        const contentElement = document.createElement('div');
        contentElement.appendChild(callback()); // Assuming callback returns an element
        window.os.gui.createWindow(emoji, title, contentElement, width, height);
    };
    
    // Call addApp with the emoji, title and initialize function 
    window.os.desktop.addApp(emoji, title, initialize);
};

```</pre>
### Library
<pre style='text-wrap: wrap'>The method signature for the `window.os.application` function is as follows:

```javascript
window.os.application : Function
    Parameters: 
        title : String
        emoji : String
        callback : Function
        width : Number (default 400)
        height : Number (default 400)
    Returns: void

```</pre>
