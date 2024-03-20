## gui_gui-styles
### Instruction: 0
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 css style for a .titleBar class to follow the following rules:
1. orange background color, a black bottom border of 1px solid
2. display of flex, a justify-content of space-between, an align-items of center
3. monospaced black small text
4. internal padding of 5px
5. render buttons flat, no background, a cursor of pointer, font size of 6, no padding
6. do not allow text selection 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here is the CSS code that meets your requirements:

```css
.titleBar {
    background-color: orange;
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: monospace;
    font-size: small;
    padding: 5px;
    user-select: none; /* This will prevent text selection */
}

/* This will apply styles to buttons inside the title bar */
.titleBar button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 6;
    padding: 0; /* This will remove default button padding */
}

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 css style for a .window class to follow the following rules:
- white background color and a padding of 1px
- a border of 2px solid black
- a border-radius of 4px
- absolute position
- display of flex and flex-direction of column
- inner .contentPlaceholder class should have a padding of 5px, flex-grow of 1 and overflow of auto
- inner .toolbarPlaceholder class should have a border-bottom of 1px solid black
- inner .statusPlaceholder class should have  a border-top of 1px solid black and a monospaced small text 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here is the CSS code that matches your requirements:

```css
.window {
    position: absolute;
    display: flex;
    flex-direction: column;
    background-color: white;
    padding: 1px;
    border: 2px solid black;
    border-radius: 4px;
}

.contentPlaceholder {
    flex-grow: 1;
    overflow: auto;
    padding: 5px;
}

.toolbarPlaceholder {
    border-bottom: 1px solid black;
}

.statusPlaceholder {
    border-top: 1px solid black;
    font-family: monospace;
    font-size: small;
}

```</pre>
### Instruction: 2
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 css style for a  `.resizeHandle` class with the following rules:
- a width and height of 10px
- an absolute position
- a bottom and right of 0
- a cursor of se-resize
- look like a resizing handle 
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here is a CSS snippet that matches your requirements:

```css
.resizeHandle {
    width: 10px;
    height: 10px;
    position: absolute;
    bottom: 0;
    right: 0;
    cursor: se-resize;
    background-color: #000; /* Change this to your desired handle color */
}

```</pre>
