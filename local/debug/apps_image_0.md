## apps_image_0
### API
<pre style='text-wrap: wrap'>/**
 * Generate an image viewer for a given path
 * @param {string} unused - Unused parameter (not used in this implementation)
 * @param {string} path - The path of the image file to view
 * @returns {HTMLImageElement} - The generated image element
 */
function imageViewer(unused, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Save the filesystem object to localStorage
 */
window.os.fs.sync = function() { ... }
/**
 * Get file content at given path
 * @param {string} path - The path to the file
 * @returns {string|undefined} - The content of the file or undefined if not found
 */
window.os.fs.getFileContentFromPath = function(path) { ... }
/**
 * Write content to a file at given path
 * @param {string} path - The path to the file
 * @param {string} content - The content to write to the file
 */
window.os.fs.write = function(path, content) { ... }
/**
 * List entries at given path
 * @param {string} path - The path to list entries at
 * @returns {Array} - An array of entries at the path or root if path is not found
 */
window.os.fs.ls = function(path = '') { ... }
/**
 * Create a directory at given path
 * @param {string} path - The path to create a directory at
 */
window.os.fs.mkdir = function(path) { ... }
/**
 * Remove a file or directory at given path
 * @param {string} path - The path to remove at
 */
window.os.fs.rm = function(path) { ... }
/**
 * Check if a path is a file
 * @param {string} path - The path to check
 * @returns {boolean} - True if path is a file, false otherwise
 */
window.os.fs.isFile = function(path) { ... }

/**
 * Register an application on the desktop.
 * 
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 * @param {number} [width=400] - The width of the application's window in pixels.
 * @param {number} [height=400] - The height of the application's window in pixels.
 * @param {Array<string>} [extensions] - The file extensions to register for this application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) { ... }



 Create a local `imageViewer` and generate jsdoc for it function that takes two parameters: `unused` and `path`  with the following functionality:
reads file content as base64 string from the path to a variable `content`
remove data:image/png;base64, or data:image/jpeg;base64 from the content
create image element with src to content
make the image fill the entire parent content
return image element 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Generate an image viewer for a given path
 * @param {string} unused - Unused parameter (not used in this implementation)
 * @param {string} path - The path of the image file to view
 * @returns {HTMLImageElement} - The generated image element
 */
function imageViewer(unused, path) {
    // Read file content as base64 string from path
    let content = window.os.fs.getFileContentFromPath(path);
    
    // Remove "data:image/png;base64," or "data:image/jpeg;base64," from content
    content = content.replace(/^data:image\/(png|jpeg);base64,/, '');
    
    // Create image element with src set to content
    let imgElement = document.createElement('img');
    imgElement.src = `data:image/png;base64,${content}`; // assuming it's a PNG image
    
    // Make the image fill the entire parent content (assuming parent is body)
    imgElement.style.width = '100%';
    imgElement.style.height = '100%';
    
    return imgElement;
}

</pre>
