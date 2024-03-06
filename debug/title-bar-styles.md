## title-bar-styles

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 css style for a .titleBar class to follow the following rules:
1. orange background color, a black bottom border of 1px solid
2. display of flex, a justify-content of space-between, an align-items of center
3. monospaced black small text
4. internal padding of 5px
5. all buttons should have a black border and small monospaced text and a rounded border of 2px, flat look
6. do not allow text selection 
### Response:

```

```
.titleBar {
    background-color: orange;
    border-bottom: 1px solid black;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: monospace;
    font-size: small;
    padding: 5px;
    user-select: none; /* This will prevent text selection */
}

/* This will apply styles to all buttons inside titleBar */
.titleBar button {
    border: 1px solid black;
    font-family: monospace;
    font-size: small;
    border-radius: 2px; /* This will give rounded corners */
}


```