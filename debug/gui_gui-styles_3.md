## gui_gui-styles_3
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>css style for `.toolbar` class to follow the following rules:
- a padding of 2px
- a background of antique white
- a margin-bottom of 2px
- a border-bottom of 1px solid black
- a display of flex
- a justify-content of flex-start
inner buttons have:
 - no border
 - cursor pointer
 - transparent background</pre>
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
.toolbar {
    padding: 2px;
    background: antiquewhite;
    margin-bottom: 2px;
    border-bottom: 1px solid black;
    display: flex;
    justify-content: flex-start;
}

.toolbar button {
    border: none;
    cursor: pointer;
    background: transparent;
}
</pre>
