## registry_extension_0
### API
<pre style='text-wrap: wrap'>/**
 * Registers an extension with an emoji and a callback function.
 * @param {string} extension - The extension to register.
 * @param {string} emoji - The emoji associated with the extension.
 * @param {function} callback - The callback function to be executed for the extension.
 */
window.os.registerExtension = function(extension, emoji, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

create a new function `registerExtension` on `window.os` object that takes an extension, an emoji and a callback function with the following functionality:
 - stores on the `window.os.registry` object the extension as key and emoji and callback as value
</pre>
### Output
<pre style='text-wrap: wrap'>// Ensure the window.os object and its registry are defined
window.os = window.os || {};
window.os.registry = window.os.registry || {};

/**
 * Registers an extension with an emoji and a callback function.
 * @param {string} extension - The extension to register.
 * @param {string} emoji - The emoji associated with the extension.
 * @param {function} callback - The callback function to be executed for the extension.
 */
window.os.registerExtension = function(extension, emoji, callback) {
    window.os.registry[extension] = {
        emoji: emoji,
        callback: callback
    };
};
</pre>
