## gui_gui-styles_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 css style for a .window class to follow the following rules:
- white background color
- disable text selection
- a border of 2px solid black
- a border-radius of 8px
- hidden overflow
- a box-shadow of 4px 4px 0 0 rgba(0,0,0,0.5)
- absolute position
- display of flex and flex-direction of column
- inner .contentPlaceholder class should have a padding of 5px, flex-grow of 1 and overflow of auto
- inner .statusPlaceholder class should have  a border-top of 1px solid black and a monospaced small text 
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

</pre>
