## gui_gui-styles_2
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

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
### Output
<pre style='text-wrap: wrap'>/* Define styles for .titleBar */
.titleBar {
    background-color: orange;
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: monospace;
    font-size: small;
    padding: 0px 5px;
    border-bottom: 2px solid black;
    user-select: none; /* Prevent text selection */
}

/* Define styles for buttons */
.titleBar button {
    border: none;
    background: none;
    cursor: pointer;
    font-size: 6px;
    padding: 5px;
}

.window {
    position: absolute;
    display: flex;
    flex-direction: column;
    border: 2px solid black;
    border-radius: 8px;
    box-shadow: 4px 4px 0 0 rgba(0,0,0,0.5);
    overflow: hidden;
    background-color: white;
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10+ */
    user-select: none; /* Standard syntax */
}

.contentPlaceholder {
    padding: 5px;
    flex-grow: 1;
    overflow: auto;
}

.statusPlaceholder {
    border-top: 1px solid black;
    font-family: monospace;
    font-size: small;
}

.resizeHandle {
    position: absolute;
    width: 0px;
    height: 0px;
    bottom: 0;
    right: 0;
    cursor: se-resize;
    border-width: 0 0 10px 10px;
    border-style: solid;
    border-color: transparent transparent #ff7200 transparent;
    transform: rotate(0deg);
}

</pre>
