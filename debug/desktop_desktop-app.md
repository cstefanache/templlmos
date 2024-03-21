## desktop_desktop-app
### Instruction: 0
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Define a function called `addApp` on `window.os.desktop` namespace that takes four parameters: emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `#desktop_content`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback 
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here is how you can define this function in JavaScript:

```javascript
// Check if os.desktop exists, if not create it
if (!window.os) {
    window.os = {};
}
if (!window.os.desktop) {
    window.os.desktop = {};
}

// Add addApp function to os.desktop
window.os.desktop.addApp = function(emoji, title, callback) {
    // Create root DOM element with class .icon
    var icon = document.createElement('div');
    icon.className = 'icon';
    
    // Create span with class .emoji and add it to icon
    var emojiSpan = document.createElement('span');
    emojiSpan.className = 'emoji';
    emojiSpan.textContent = emoji;
    icon.appendChild(emojiSpan);
    
    // Create span with class .title and add it to icon
    var titleSpan = document.createElement('span');
    titleSpan.className = 'title';
    titleSpan.textContent = title;
    icon.appendChild(titleSpan);
    
    // Append icon to #desktop_content
    document.querySelector('#desktop_content').appendChild(icon);
    
    // Add click event listener to icon
    icon.addEventListener('click', function() {
        // Call callback when icon is clicked
        if (typeof callback === 'function') {
            callback();
        }
    });
};

```</pre>
### Library
<pre style='text-wrap: wrap'>The method signature for the `window.os.desktop.addApp` function is as follows:

```javascript
function addApp(emoji: string, title: string, callback: Function): void;

```</pre>
