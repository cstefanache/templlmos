## minesweeper-desktop-icon

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that executes `os.gui.addIcon('Minesweeper', '💣', () => os.apps.minesweeper(), document.body)` 
### Response:

```

```
(function() {
    os.gui.addIcon('Minesweeper', '💣', () => os.apps.minesweeper(), document.body);
})();


```