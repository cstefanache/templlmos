## gui_gui-styles_2
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers.

css style for a  `.resizeHandle` class with the following rules:
- a width and height of 0px
- an absolute position
- a bottom and right of 0
- a cursor of se-resize
- border width: 0 0 10px 10px
- border style: solid
- `border-color: transparent transparent #ff7200 transparent`
- transform: rotate(0deg)
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
.resizeHandle {
    width: 0;
    height: 0;
    position: absolute;
    bottom: 0;
    right: 0;
    cursor: se-resize;
    border-width: 0 0 10px 10px;
    border-style: solid;
    border-color: transparent transparent #ff7200 transparent;
    transform: rotate(0deg);
}
</pre>
