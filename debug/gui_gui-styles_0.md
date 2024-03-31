## gui_gui-styles_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 css style for a .titleBar class to follow the following rules:
- orange background color, a black bottom border of 1px solid
- display of flex, a justify-content of space-between, an align-items of center
- monospaced black small text
- 5px horizontal padding, 0 vertical padding
- 2px black border bottom
- render buttons flat, no border, no background, a cursor of pointer, font size of 6, 5px padding
- do not allow text selection 
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

</pre>
