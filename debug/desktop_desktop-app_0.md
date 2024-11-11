## desktop_desktop-app_0
### API
<pre style='text-wrap: wrap'>/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to be displayed in the icon.
 * @param {string} title - The title to be displayed in the icon.
 * @param {Function} callback - The function to be called when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Define a function called `addApp` on `window.os` namespace that takes four parameters: emoji, title and a callback:
- call `icon` with element at `#desktop_content`, emoji, title and the callback as parameters</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to be displayed in the icon.
 * @param {string} title - The title to be displayed in the icon.
 * @param {Function} callback - The function to be called when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) {
    const parent = document.getElementById('desktop_content');
    window.os.icon(parent, emoji, title, callback);
};
</pre>
