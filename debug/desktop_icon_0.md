## desktop_icon_0
### API
<pre style='text-wrap: wrap'>    /**
     * Creates an icon element with an emoji and title, and attaches a click event.
     * @param {HTMLElement} parent - The parent element to which the icon will be appended.
     * @param {string} emoji - The emoji to display in the icon.
     * @param {string} title - The title to display in the icon.
     * @param {Function} callback - The function to call when the icon is clicked.
     */
window.os.icon = function(parent, emoji, title, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Define a function called `icon` on `window.os` namespace that takes three parameters: parent, emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `parent`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback
</pre>
### Output
<pre style='text-wrap: wrap'>(function() {
    window.os = window.os || {};

    /**
     * Creates an icon element with an emoji and title, and attaches a click event.
     * @param {HTMLElement} parent - The parent element to which the icon will be appended.
     * @param {string} emoji - The emoji to display in the icon.
     * @param {string} title - The title to display in the icon.
     * @param {Function} callback - The function to call when the icon is clicked.
     */
    window.os.icon = function(parent, emoji, title, callback) {
        var iconElement = document.createElement('div');
        iconElement.className = 'icon';

        var emojiElement = document.createElement('span');
        emojiElement.className = 'emoji';
        emojiElement.textContent = emoji;

        var titleElement = document.createElement('span');
        titleElement.className = 'title';
        titleElement.textContent = title;

        iconElement.appendChild(emojiElement);
        iconElement.appendChild(titleElement);
        parent.appendChild(iconElement);

        iconElement.addEventListener('click', callback);
    };
})();
</pre>
