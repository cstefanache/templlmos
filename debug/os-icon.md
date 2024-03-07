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
Append to `.emoji` class list the concatenation between the `icon-` and the extension extracted from `name` if the name contains the dot character 
### Response:

```

```
(function() {
    if (!window.os) window.os = {};
    if (!window.os.gui) window.os.gui = {};
    
    window.os.gui.addIcon = function(name, icon, callback, container) {
        // create root element
        var root = document.createElement('div');
        root.classList.add('icon');
        
        // create emoji element
        var emoji = document.createElement('div');
        emoji.classList.add('emoji');
        
        // create app-name element
        var appName = document.createElement('div');
        appName.classList.add('app-name');
        appName.textContent = name;
        
        // add icon to emoji element
        emoji.textContent = icon;
        
        // add event listener to root element
        root.addEventListener('click', callback);
        
        // add elements to root element
        root.appendChild(emoji);
        root.appendChild(appName);
        
        // add icon to container
        container.appendChild(root);
        
        // add icon-* class to emoji element if name contains dot character
        if (name.includes('.')) {
            var extension = name.split('.').pop();
            emoji.classList.add('icon-' + extension);
        }
    };
})();


```