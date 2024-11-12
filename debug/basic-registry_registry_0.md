## basic-registry_registry_0
### API

<pre style='text-wrap: wrap'>
/**
 * Registers a new application in the OS with a title, emoji, and a callback function.
 * The callback function should return a DOM element that will be displayed in the body.
 * A close button will be added to allow removal of the application from the body.
 * 
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji representing the application.
 * @param {function} callback - A function that returns a DOM element to be displayed.
 */
window.os.registerApplication = function(title, emoji, callback) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
create a new function `registerApplication` on the `window.os` object and jsdoc that takes a title, emoji, callback by default having the following functionality:
- execute the callback function and store the resulting DOM element in a variable
- set position relative to the DOM element
- create a new span dom element with the class .close-button and text: ❌, append it to the DOM element and add a click event listener that removes the DOM element from the body
- append the DOM element to the body
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Registers a new application in the OS with a title, emoji, and a callback function.
 * The callback function should return a DOM element that will be displayed in the body.
 * A close button will be added to allow removal of the application from the body.
 * 
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji representing the application.
 * @param {function} callback - A function that returns a DOM element to be displayed.
 */
window.os = window.os || {};

window.os.registerApplication = function(title, emoji, callback) {
    const appElement = callback();
    appElement.style.position = 'relative';

    const closeButton = document.createElement('span');
    closeButton.className = 'close-button';
    closeButton.textContent = '❌';
    closeButton.addEventListener('click', function() {
        document.body.removeChild(appElement);
    });

    appElement.appendChild(closeButton);
    document.body.appendChild(appElement);
};

</pre>
