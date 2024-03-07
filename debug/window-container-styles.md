## window-container-styles

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
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

```

```
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


```