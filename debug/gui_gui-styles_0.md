## gui_gui-styles_0
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
css style for a .titleBar class to follow the following rules:
- orange background color, a black bottom border of 1px solid
- display of flex, a justify-content of space-between, an align-items of center
- monospaced black small text
- 5px horizontal padding, 0 vertical padding
- 2px black border bottom
- render buttons flat, no border, no background, a cursor of pointer, font size of 6, 5px padding
- do not allow text selection
</pre>
### Output

<pre style='text-wrap: wrap'>
.titleBar {
    background-color: orange;
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: monospace;
    color: black;
    font-size: small;
    padding: 0 5px;
    border-bottom: 2px solid black;
    user-select: none;
}

.titleBar button {
    border: none;
    background: none;
    cursor: pointer;
    font-size: 6px;
    padding: 5px;
}

</pre>
