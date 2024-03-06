## desktop-icons

### Instruction
```
Generate code only. Stop after the code is generated. Do not provide any explanations.
### Instruction:
 css style the `.icon` class to match the following rules:
1. 64x64px size, text-align center, margin of 5px, pointer cursor
2. containing `.emoji` class should be a block, have a font-size of 30px
3. containing `.app-name` class should be a block, have a font-size of 8px, black background,  monospaced font, white text, padding of 5px, allow word-wrap to break word 
### Response:

```

```
.icon {
    width: 64px;
    height: 64px;
    text-align: center;
    margin: 5px;
    cursor: pointer;
}

.emoji {
    display: block;
    font-size: 30px;
}

.app-name {
    display: block;
    font-size: 8px;
    background-color: black;
    color: white;
    font-family: monospace;
    padding: 5px;
    word-wrap: break-word;
}


```