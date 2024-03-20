## gui_gui-tests
### Instruction: 0
<pre style='text-wrap: wrap'>The provided JavaScript code defines four functions on the `window.os.gui` object: 

1. `makeDraggable(root, dragHandle)`: This function makes an element draggable by setting up event listeners for mouse events that allow for dragging of the element when the drag handle (provided as an argument to the function) is clicked and dragged over. The element's position is updated in real-time as the mouse moves, and it stops being dragged when the mouse button is released.

2. `makeResizable(root, resizeHandle)`: This function makes an element resizable by setting up event listeners for mouse events that allow for resizing of the element when the resize handle (provided as an argument to the function) is clicked and dragged over. The element's width and height are updated in real-time as the mouse moves, and it stops being resized when the mouse button is released.

3. `bringToFront(rootDomNode)`: This function brings a specified DOM node to the front of other nodes with the same class by setting their z-index to 0, then setting the z-index of the rootDomNode to 1. This effectively places it in front of all other nodes with the same class.

4. The last part of your code checks if the `window.os` and `window.os.gui` objects exist, creating them if they don't, before assigning these four functions to them. This ensures that these objects exist before any of these functions are called, preventing potential errors if they are called before these objects are initialized. 

In summary, this code provides a set of utility functions for creating draggable, resizable, and front-bringing elements in a web page, which can be useful for creating user interfaces or other interactive web applications.

``` Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 create a DOM element, absolute position, 100x100px, background color red, append to body
add another DOM element to the first one, relative position, width:100% height:20px, background color blue, append to first one
call make draggable the first element by the second one
add another DOM element to the first one, absolute position, right:0, bottom:0, width:10px height:10px, background color green, append to first one
call make resizable the first element by the third one 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here is a simple example of how you can achieve this using vanilla JavaScript:

```javascript
// Create a new div and set its properties
let div = document.createElement('div');
div.style.position = 'absolute';
div.style.width = '100px';
div.style.height = '100px';
div.style.backgroundColor = 'red';
document.body.appendChild(div);

// Create another div and set its properties and append it to the first div
let div2 = document.createElement('div');
div2.style.position = 'relative';
div2.style.width = '100%';
div2.style.height = '20px';
div2.style.backgroundColor = 'blue';
div.appendChild(div2);

// Create another div and set its properties and append it to the first div
let div3 = document.createElement('div');
div3.style.position = 'absolute';
div3.style.right = '0';
div3.style.bottom = '0';
div3.style.width = '10px';
div3.style.height = '10px';
div3.style.backgroundColor = 'green';
div.appendChild(div3);

// Make the first div draggable using the second div as the drag handle
if (!window.os || !window.os.gui || !window.os.gui.makeDraggable) {
    window.os = window.os || {};
    window.os.gui = window.os.gui || {};
    window.os.gui.makeDraggable = (function() {
        var startX, startY, startLeft, startTop;
        return function(root, dragHandle) {
            var rect = root.getBoundingClientRect();
            startLeft = rect.left;
            startTop = rect.top;
            dragHandle.addEventListener('mousedown', function(e) {
                startX = e.clientX;
                startY = e.clientY;
                document.addEventListener('mousemove', move);
                document.addEventListener('mouseup', up);
            });
            function move(e) {
                var left = startLeft + e.clientX - startX;
                var top = startTop + e.clientY - startY;
                root.style.left = left + 'px';
                root.style.top = top + 'px';
            }
            function up() {
                document.removeEventListener('mousemove', move);
                document.removeEventListener('mouseup', up);
            }
        };
    })();
}
window.os.gui.makeDraggable(div, div2);

// Make the first div resizable using the third div as the resize handle
if (!window.os || !window.os.gui || !window.os.gui.makeResizable) {
    window.os = window.os || {};
    window.os.gui = window.os.gui || {};
    window.os.gui.makeResizable = (function() {
        var startWidth, startHeight;
        return function(root, resizeHandle) {
            var rect = root.getBoundingClientRect();
            startWidth = rect.width;
            startHeight = rect.height;
            resizeHandle.addEventListener('mousedown', function(e) {
                document.addEventListener('mousemove', move);
                document.addEventListener('mouseup', up);
            });
            function move(e) {
                var width = startWidth + e.clientX - resizeHandle.getBoundingClientRect().left;
                var height = startHeight + e.clientY - resizeHandle.getBoundingClientRect().top;
                root.style.width = width + 'px';
                root.style.height = height + 'px';
            }
            function up() {
                document.removeEventListener('mousemove', move);
                document.removeEventListener('mouseup', up);
            }
        };
    })();
}
window.os.gui.makeResizable(div, div3);

```</pre>
