## apps_image_0
### API
<pre style='text-wrap: wrap'>/**
 * Creates an image viewer that displays an image from a given path.
 * @param {any} unused - Unused parameter.
 * @param {string} path - The path to the image file.
 * @returns {HTMLImageElement} - The image element that displays the image.
 */
window.imageViewer = function(unused, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.

Given the following implemented functions:
    /**
     * Saves the filesystem object to local storage.
     * @function
     */
window.os.fs.sync = function() { ... }
    /**
     * Processes and returns a path, handling '..', '//' and '/'.
     * @param {string} path - The path to process.
     * @returns {string|null} - The processed path or null if invalid.
     */
window.os.fs.getPath = function(path) { ... }
    /**
     * Checks if the path is valid.
     * @param {string} path - The path to check.
     * @returns {boolean} - True if valid, false otherwise.
     */
window.os.fs.isValidPath = function(path) { ... }
    /**
     * Returns a list of entries in the filesystem object at the given path.
     * @param {string} path - The path to list entries from.
     * @returns {Array} - An array of entries.
     */
window.os.fs.ls = function(path) { ... }
    /**
     * Creates an empty object at the given path.
     * @param {string} path - The path to create the directory at.
     */
window.os.fs.mkdir = function(path) { ... }
    /**
     * Removes the object at the given path.
     * @param {string} path - The path to remove the object from.
     */
window.os.fs.rm = function(path) { ... }
    /**
     * Writes the content to an entry in the filesystem object at the given path.
     * @param {string} path - The path to write to.
     * @param {string} content - The content to write.
     */
window.os.fs.write = function(path, content) { ... }
    /**
     * Reads an entry split by '\n' in the filesystem object at the given path.
     * @param {string} path - The path to read from.
     * @returns {Array|null} - An array of lines or null if not found.
     */
window.os.fs.read = function(path) { ... }

/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to display for the application.
 * @param {Function} callback - The function to call when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions=undefined] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions = undefined) { ... }



Create a local `imageViewer` and generate jsdoc for it function that takes two parameters: `unused` and `path`  with the following functionality:
reads file content as base64 string from the path to a variable `content`
remove data:image/png;base64, or data:image/jpeg;base64 from the content
create image element with src to content
make the image fill the entire parent content
return image element
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Creates an image viewer that displays an image from a given path.
 * @param {any} unused - Unused parameter.
 * @param {string} path - The path to the image file.
 * @returns {HTMLImageElement} - The image element that displays the image.
 */
window.imageViewer = function(unused, path) {
    const content = window.os.fs.read(path);
    if (content) {
        const base64Content = content.join('\n').replace(/^data:image\/(png|jpeg);base64,/, '');
        const img = document.createElement('img');
        img.src = 'data:image/png;base64,' + base64Content;
        img.style.width = '100%';
        img.style.height = '100%';
        img.style.objectFit = 'cover';
        return img;
    }
    return null;
};

// Register the image viewer application
window.os.registerApplication('Image Viewer', '🖼️', window.imageViewer);
</pre>
