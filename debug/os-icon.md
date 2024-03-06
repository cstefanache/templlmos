## os-icon

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `addIcon` on the `window.os.gui` object
The `addIcon` function takes 3 arguments: `name`, `icon`, `callback` and `container`
The `name` argument is a string that represents the name of the icon
The `icon` argument is a string that represents the icon
The `callback` argument is a function that is called when the icon is clicked
The `container` argument represents the DOM element of the container where the icon should be appended
The created root element should have the class `.icon`, and should contain two child elements: `.emoji` and `.app-name` 
### Response:

```

```
(function() {
    if (!window.os) {
        window.os = {};
    }
    if (!window.os.gui) {
        window.os.gui = {};
    }
    window.os.gui.addIcon = function(name, icon, callback, container) {
        var root = document.createElement('div');
        root.classList.add('icon');
        
        var emoji = document.createElement('span');
        emoji.classList.add('emoji');
        emoji.textContent = icon;
        root.appendChild(emoji);
        
        var appName = document.createElement('span');
        appName.classList.add('app-name');
        appName.textContent = name;
        root.appendChild(appName);
        
        root.addEventListener('click', callback);
        
        container.appendChild(root);
    };
})();


```