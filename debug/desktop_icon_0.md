## desktop_icon_0
### API

<pre style='text-wrap: wrap'>
    /**
     * Creates an icon element with an emoji and title, and attaches a click event.
     * @param {HTMLElement} parent - The parent element to which the icon will be appended.
     * @param {string} emoji - The emoji to display in the icon.
     * @param {string} title - The title to display in the icon.
     * @param {function} callback - The function to call when the icon is clicked.
     */
window.os.icon = function(parent, emoji, title, callback) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Define a function called `icon` on `window.os` namespace that takes three parameters: parent, emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `parent`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback
</pre>
### Output

<pre style='text-wrap: wrap'>
(function() {
    window.os = window.os || {};

    /**
     * Creates an icon element with an emoji and title, and attaches a click event.
     * @param {HTMLElement} parent - The parent element to which the icon will be appended.
     * @param {string} emoji - The emoji to display in the icon.
     * @param {string} title - The title to display in the icon.
     * @param {function} callback - The function to call when the icon is clicked.
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
