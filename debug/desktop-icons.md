## desktop-icons

### Instruction
```
Generate code only. Stop after the code is generated. Do not provide any explanations.
### Instruction:
 css style the `.icon` class to match the following rules:
1. 64px width, 64px min height, text-align center, margin of 5px, pointer cursor
2. containing `.emoji` class should be a block, have a font-size of 30px and inline-block display, position relative
3. containing `.app-name` class should be a block, have a font-size of 8px, monospaced font, black text, padding of 5px, allow word-wrap to break word 
### Response:

```

```
.icon {
    width: 64px;
    min-height: 64px;
    text-align: center;
    margin: 5px;
    cursor: pointer;
}

.emoji {
    display: inline-block;
    font-size: 30px;
    position: relative;
}

.app-name {
    display: block;
    font-size: 8px;
    font-family: monospace;
    color: black;
    padding: 5px;
    word-wrap: break-word;
}


```