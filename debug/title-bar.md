## title-bar

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that defines a function called `titleBar` on the `window.os.gui` object having the following functionality:
- create a root DOM element with the class `.titleBar`
- add to the root DOM element a `span` containing the title parameter
- add to the root DOM element a `button` with the text `x`
- when the button is clicked then the DOM element passed as the second parameter should be removed from the body
- when root DOM element is dragged then move the DOM element passed as the second parameter
- return the root DOM element 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.gui = window.os.gui || {};
    window.os.gui.titleBar = function(title, targetElement) {
        // Create root DOM element
        var titleBar = document.createElement('div');
        titleBar.className = 'titleBar';
        
        // Add title to span and append to titleBar
        var titleSpan = document.createElement('span');
        titleSpan.textContent = title;
        titleBar.appendChild(titleSpan);
        
        // Add button to titleBar
        var closeButton = document.createElement('button');
        closeButton.textContent = 'x';
        closeButton.addEventListener('click', function() {
            document.body.removeChild(targetElement);
        });
        titleBar.appendChild(closeButton);
        
        // Add drag and drop functionality to titleBar
        var dragging = false;
        var startX;
        var startY;
        var offsetX;
        var offsetY;
        
        titleBar.addEventListener('mousedown', function(e) {
            dragging = true;
            startX = e.clientX;
            startY = e.clientY;
            offsetX = targetElement.offsetLeft;
            offsetY = targetElement.offsetTop;
        });
        
        titleBar.addEventListener('mouseup', function() {
            dragging = false;
        });
        
        titleBar.addEventListener('mousemove', function(e) {
            if (dragging) {
                var x = e.clientX - startX;
                var y = e.clientY - startY;
                targetElement.style.left = (offsetX + x) + 'px';
                targetElement.style.top = (offsetY + y) + 'px';
            }
        });
        
        return titleBar;
    };
})();


```