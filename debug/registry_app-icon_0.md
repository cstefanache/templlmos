## registry_app-icon_0
### API

<pre style='text-wrap: wrap'>
/**
 * Creates an OS icon element for a given path and sets up a click callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The function to call when the icon is clicked.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) { ... }
currentCallback = function() { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
create jsdoc and function `getOSIcon` on `window.os` object having a path and callback parameter with the following functionality:
- create a root element `div` having the class `icon`
- save isFile to constant
- add a span element with class `emoji` and content 📄 if isFile, 📁 otherwise
- add a div element with class title containing the name from path
- extract extension from path and search if is registered in the `window.os.registry` object
- sets `currentCallback` to function parameter callback
- if extension is registered reads stores it in a `extData` property and:
   - adds span element with class `app-emoji` with the content of `extData.emoji` 
   - sets the `currentCallback` to a function that calls `extData.callback` with the path
- exit condition and add click listener to the root element that calls `currentCallback` with the path
- return the root element
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Creates an OS icon element for a given path and sets up a click callback.
 * @param {string} path - The path for which to create the icon.
 * @param {function} callback - The function to call when the icon is clicked.
 * @returns {HTMLElement} - The root icon element.
 */
window.os.getOSIcon = function(path, callback) {
    const iconElement = document.createElement('div');
    iconElement.className = 'icon';

    const isFile = path.includes('.'); // Simple check for file extension
    const emojiSpan = document.createElement('span');
    emojiSpan.className = 'emoji';
    emojiSpan.textContent = isFile ? '📄' : '📁';
    iconElement.appendChild(emojiSpan);

    const titleDiv = document.createElement('div');
    titleDiv.className = 'title';
    titleDiv.textContent = path.split('/').pop(); // Get the name from the path
    iconElement.appendChild(titleDiv);

    const extension = isFile ? path.split('.').pop() : null;
    let currentCallback = callback;

    if (extension && window.os.registry && window.os.registry[extension]) {
        const extData = window.os.registry[extension];
        const appEmojiSpan = document.createElement('span');
        appEmojiSpan.className = 'app-emoji';
        appEmojiSpan.textContent = extData.emoji;
        iconElement.appendChild(appEmojiSpan);

        currentCallback = function() {
            extData.callback(path);
        };
    }

    iconElement.addEventListener('click', function() {
        currentCallback(path);
    });

    return iconElement;
};

</pre>
