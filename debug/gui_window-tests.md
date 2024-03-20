## gui_window-tests
### Instruction: 0
<pre style='text-wrap: wrap'>The function `window.os.gui.createWindow` is a JavaScript function that creates a new GUI window with various components such as title bar, toolbar, content area, status bar, and a resize handle. The function takes in several parameters including emoji for the title bar, title of the window, content to be displayed in the content area, width of the window, and height of the window. The function returns null after creating the window. 

Here is the function signature:

```javascript
window.os.gui.createWindow(emoji?: string, title?: string, content?: Node | null, width?: number, height?: number): null;

``` Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a new window with the title `My Window` and a div containing `hello world 1` as content having 😃 as emoji
Create a new window with the title `My Window 2` and a div containing  `hello world 2` as content having 💄 as emoji 
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here's how you can create two windows using your specifications:

```javascript
// Create first window
let div1 = document.createElement('div');
div1.innerHTML = 'hello world 1';
let win1 = window.os.gui.createWindow('😃', 'My Window', div1);

// Create second window
let div2 = document.createElement('div');
div2.innerHTML = 'hello world 2';
let win2 = window.os.gui.createWindow('💄', 'My Window 2', div2);

```</pre>
