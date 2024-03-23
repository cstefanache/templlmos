## gui_gui-styles
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 css style for a .titleBar class to follow the following rules:
- orange background color, a black bottom border of 1px solid
- display of flex, a justify-content of space-between, an align-items of center
- monospaced black small text
- internal padding of 5px
- 2px black border bottom
- render buttons flat, no border, no background, a cursor of pointer, font size of 6, no padding
- do not allow text selection 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is the CSS code you requested:

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
    border-bottom: 2px solid black;
    user-select: none; /* This will prevent text selection */
}

/* This will apply styles to buttons inside titleBar */
.titleBar button {
    border: none;
    background: none;
    cursor: pointer;
    font-size: 6px;
    padding: 0;
}

```</pre>
### Instruction: 2
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 css style for a .window class to follow the following rules:
- white background color and a padding of 1px
- a border of 2px solid black
- a border-radius of 8px
- no padding
- hidden overflow
- a box-shadow of 4px 4px 0 0 rgba(0,0,0,0.5)
- absolute position
- display of flex and flex-direction of column
- inner .contentPlaceholder class should have a padding of 5px, flex-grow of 1 and overflow of auto
- inner .statusPlaceholder class should have  a border-top of 1px solid black and a monospaced small text 
### Response:
</pre>
#### Output: 1
<pre style='text-wrap: wrap'>Here is your CSS code:

```css
.window {
    position: absolute;
    display: flex;
    flex-direction: column;
    background-color: white;
    padding: 0;
    border: 2px solid black;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 4px 4px 0 0 rgba(0,0,0,0.5);
}

.contentPlaceholder {
    flex-grow: 1;
    overflow: auto;
    padding: 5px;
}

.statusPlaceholder {
    border-top: 1px solid black;
    font-family: monospace;
    font-size: small;
}

```</pre>
### Instruction: 3
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 css style for a  `.resizeHandle` class with the following rules:
- a width and height of 0px
- an absolute position
- a bottom and right of 0
- a cursor of se-resize
- border width: 0 0 10px 10px
- border style: solid
- `border-color: transparent transparent #ff7200 transparent`
- transform: rotate(0deg) 
### Response:
</pre>
#### Output: 2
<pre style='text-wrap: wrap'>Sure, here is your CSS code:

```css
.resizeHandle {
    width: 0px;
    height: 0px;
    position: absolute;
    bottom: 0;
    right: 0;
    cursor: se-resize;
    border-width: 0 0 10px 10px;
    border-style: solid;
    border-color: transparent transparent #ff7200 transparent;
    transform: rotate(0deg);
}

```</pre>
### Instruction: 4
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 css style for a .toolbar class to follow the following rules:
- a padding of 2px
- a background of antique white
- a margin-bottom of 2px
- a border-bottom of 1px solid black
- a display of flex
- a justify-content of flex-start
inner buttons have:
 - no border
 - cursor pointer
 - transparent background 
### Response:
</pre>
#### Output: 3
<pre style='text-wrap: wrap'>Sure, here is the CSS code you requested:

```css
.toolbar {
    display: flex;
    justify-content: flex-start;
    padding: 2px;
    background-color: antiquewhite;
    margin-bottom: 2px;
    border-bottom: 1px solid black;
}

.toolbar button {
    border: none;
    cursor: pointer;
    background-color: transparent;
}

```</pre>
