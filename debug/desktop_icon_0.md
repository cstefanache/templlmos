## desktop_icon_0
### API
<pre style='text-wrap: wrap'>/**
 * Create an icon element with an emoji and a tooltip.
 * @param {HTMLElement} parent - The parent element to append this icon to.
 * @param {string} emoji - The emoji to display in this icon.
 * @param {string} title - The tooltip text to display when hovering over this icon.
 * @param {function} callback - The callback to call when this icon is clicked.
 */
window.os.icon = function(parent, emoji, title, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 Define a function called `icon` on `window.os` namespace that takes three parameters: parent, emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `parent`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Check if window.os exists, if not create it
if (!window.os) {
    window.os = {};
}

/**
 * Create an icon element with an emoji and a tooltip.
 * @param {HTMLElement} parent - The parent element to append this icon to.
 * @param {string} emoji - The emoji to display in this icon.
 * @param {string} title - The tooltip text to display when hovering over this icon.
 * @param {function} callback - The callback to call when this icon is clicked.
 */
window.os.icon = function(parent, emoji, title, callback) {
    // Create root DOM element with class .icon
    var icon = document.createElement('div');
    icon.classList.add('icon');
    
    // Create span with class .emoji and add it to icon
    var emojiSpan = document.createElement('span');
    emojiSpan.classList.add('emoji');
    emojiSpan.textContent = emoji;
    icon.appendChild(emojiSpan);
    
    // Create span with class .title and add it to icon
    var titleSpan = document.createElement('span');
    titleSpan.classList.add('title');
    titleSpan.textContent = title;
    icon.appendChild(titleSpan);
    
    // Add click event listener to icon
    icon.addEventListener('click', callback);
    
    // Append icon to parent
    parent.appendChild(icon);
};

</pre>
