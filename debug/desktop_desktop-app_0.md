## desktop_desktop-app_0
### API
<pre style='text-wrap: wrap'>/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to display in the icon.
 * @param {string} title - The title to display in the icon.
 * @param {Function} callback - The function to call when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Given the following implemented functions:
    /**
     * Creates an icon element with an emoji and title, and attaches a click event.
     * @param {HTMLElement} parent - The parent element to which the icon will be appended.
     * @param {string} emoji - The emoji to display in the icon.
     * @param {string} title - The title to display in the icon.
     * @param {Function} callback - The function to call when the icon is clicked.
     */
window.os.icon = function(parent, emoji, title, callback) { ... }



Define a function called `addApp` on `window.os` namespace that takes four parameters: emoji, title and a callback:
- call `icon` with element at `#desktop_content`, emoji, title and the callback as parameters
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to display in the icon.
 * @param {string} title - The title to display in the icon.
 * @param {Function} callback - The function to call when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) {
    const parent = document.getElementById('desktop_content');
    window.os.icon(parent, emoji, title, callback);
};
</pre>
