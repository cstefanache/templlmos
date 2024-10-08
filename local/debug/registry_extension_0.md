## registry_extension_0
### API
<pre style='text-wrap: wrap'>/**
 * Register an extension with its corresponding emoji and callback.
 * @param {string} extension - The name of the extension to register.
 * @param {string} emoji - The corresponding emoji for this extension.
 * @param {function} callback - The callback to be executed when this extension is used.
 */
window.os.registerExtension = function(extension, emoji, callback) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 create a new function `registerExtension` on `window.os` object that takes an extension, an emoji and a callback function with the following functionality:
 - stores on the `window.os.registry` object the extension as key and emoji and callback as value 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Assuming window.os is already defined
if (!window.os) {
    window.os = {};
}

// Assuming window.os.registry is already defined
if (!window.os.registry) {
    window.os.registry = {};
}

/**
 * Register an extension with its corresponding emoji and callback.
 * @param {string} extension - The name of the extension to register.
 * @param {string} emoji - The corresponding emoji for this extension.
 * @param {function} callback - The callback to be executed when this extension is used.
 */
window.os.registerExtension = function(extension, emoji, callback) {
    window.os.registry[extension] = {emoji: emoji, callback: callback};
};

</pre>
