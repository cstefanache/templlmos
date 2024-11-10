## apps_photobooth_1
### API
<pre style='text-wrap: wrap'></pre>
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

/**
 * Creates a toolbar and appends it to the specified window element.
 * @param {HTMLElement} win - The window element to which the toolbar will be appended.
 * @returns {function(string, function): void} - A function to add buttons to the toolbar.
 */
window.os.gui.createToolbar = function(win) { ... }
    /**
     * Adds a button to the toolbar.
     * @param {string} text - The text to display on the button.
     * @param {function} callback - The function to call when the button is clicked.
     */

/**
 * Displays a notification with the given message.
 * @param {string} message - The message to display in the notification.
 */
window.os.gui.notification = function(message) { ... }

function photoBooth(win) { ... }


call register application with 'Photobooth' title, 📸 as emoji, function reference and 410x360 size
</pre>
### Output
<pre style='text-wrap: wrap'>function photoBooth(win) {
    const root = document.createElement('div');
    const toolbar = window.os.gui.createToolbar(win);
    
    const video = document.createElement('video');
    video.autoplay = true;
    root.appendChild(video);
    
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(error => {
            console.error('Error accessing webcam:', error);
        });

    toolbar('📸', () => {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0);
        
        const timestamp = Date.now();
        const path = `photobooth/image+${timestamp}.png`;
        canvas.toBlob(blob => {
            const reader = new FileReader();
            reader.onloadend = () => {
                window.os.fs.write(path, reader.result);
                window.os.gui.notification(`Snapshot saved to ${path}`);
            };
            reader.readAsDataURL(blob);
        });
    });

    return root;
}
window.os.registerApplication('Photobooth', '📸', photoBooth, 410, 360);
</pre>
