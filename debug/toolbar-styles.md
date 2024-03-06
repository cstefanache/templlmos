## toolbar-styles

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 css style for a .toolbar class to follow the following rules:
- a padding of 3px 5px
- a margin-bottom of 2px
- a display of flex
- a justify-content of flex-start
inner buttons have:
 - no border
 - cursor pointer
 - a white background and a light gray on hover 
### Response:

```

```
.toolbar {
    padding: 3px 5px;
    margin-bottom: 2px;
    display: flex;
    justify-content: flex-start;
}

.toolbar button {
    border: none;
    cursor: pointer;
    background-color: white;
}

.toolbar button:hover {
    background-color: lightgray;
}


```