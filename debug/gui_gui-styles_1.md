## gui_gui-styles_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers.

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
</pre>
### Output
<pre style='text-wrap: wrap'>.titleBar {
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
.window {
    background-color: white;
    user-select: none;
    border: 2px solid black;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 4px 4px 0 0 rgba(0, 0, 0, 0.5);
    position: absolute;
    display: flex;
    flex-direction: column;
}

.window .contentPlaceholder {
    padding: 5px;
    flex-grow: 1;
    overflow: auto;
}

.window .statusPlaceholder {
    border-top: 1px solid black;
    font-family: monospace;
    font-size: small;
}
</pre>
