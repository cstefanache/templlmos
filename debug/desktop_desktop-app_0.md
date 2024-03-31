## desktop_desktop-app_0
### API
<pre style='text-wrap: wrap'>/**
 * Adds an application to the desktop content.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Create an icon element with an emoji and a tooltip.
 * @param {HTMLElement} parent - The parent element to append this icon to.
 * @param {string} emoji - The emoji to display in this icon.
 * @param {string} title - The tooltip text to display when hovering over this icon.
 * @param {function} callback - The callback to call when this icon is clicked.
 */
window.os.icon = function(parent, emoji, title, callback) { ... }



 Define a function called `addApp` on `window.os` namespace that takes four parameters: emoji, title and a callback:
- call `icon` with element at `#desktop_content`, emoji, title and the callback as parameters 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Adds an application to the desktop content.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) {
    window.os.icon(document.querySelector('#desktop_content'), emoji, title, callback);
};

</pre>
