## undefined

### Instruction
```
Generate css code without the use of any library or framework.
### Instruction:
 None 
### Response:

```

```
function createCSS(selector, rules) {
    var style = document.createElement('style');
    style.type = 'text/css';
    
    if (style.styleSheet){
        // This is required for IE8 and below.
        style.styleSheet.cssText = selector + '{' + rules + '}';
    } else {
        style.appendChild(document.createTextNode(selector + '{' + rules + '}'));
    }
    
    document.getElementsByTagName('head')[0].appendChild(style);
}

createCSS('.myClass', 'color: red; background-color: blue;');


```