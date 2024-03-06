## add browser to desktop

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that executes `os.gui.addIcon('Browser', '📁', () => os.apps.browser(''), document.body)` 
### Response:

```

```
(function() {
    os.gui.addIcon('Browser', '📁', () => os.apps.browser(''), document.body);
})();


```