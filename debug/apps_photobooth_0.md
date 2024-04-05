## apps_photobooth_0
### API
<pre style='text-wrap: wrap'>function createPhotoBooth() { ... }
function takeSnapshot(videoElement) { ... }
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

window.os.gui.notification = function(message) { ... }



 create a local photoBooth function that takes no parameters:
- create a root dom element, do not style it
- append browser webcam capture video element with autoplay on
- add a button with text 'Take Snapshot' that takes an image snapshot of the video and saves it to 'photobooth/image+{timestamp}.png' and notify the user: 'Snapshot saved to {path}'
- return root dom element 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>function createPhotoBooth() {
    // Create root DOM element
    const rootElement = document.createElement('div');
    
    // Append video element with autoplay on
    const videoElement = document.createElement('video');
    videoElement.autoplay = true;
    videoElement.width = 400; // Set width of video element
    videoElement.height = 300; // Set height of video element
    rootElement.appendChild(videoElement);
    
    // Add button with text 'Take Snapshot'
    const buttonElement = document.createElement('button');
    buttonElement.innerText = 'Take Snapshot';
    buttonElement.onclick = () => takeSnapshot(videoElement); // Call takeSnapshot function when button is clicked
    rootElement.appendChild(buttonElement);
    
    // Request access to camera
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => videoElement.srcObject = stream)
        .catch(err => console.error('Error accessing camera', err));
    
    return rootElement;
}

function takeSnapshot(videoElement) {
    // Create canvas element
    const canvasElement = document.createElement('canvas');
    canvasElement.width = videoElement.videoWidth; // Set width of canvas element to match video element's width
    canvasElement.height = videoElement.videoHeight; // Set height of canvas element to match video element's height
    
    // Draw video frame on canvas
    const context = canvasElement.getContext('2d');
    context.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
    
    // Convert canvas image to data URL
    const imageDataUrl = canvasElement.toDataURL('image/png');
    
    // Generate timestamp for filename
    const timestamp = Date.now();
    
    // Generate path for image save
    const path = `photobooth/image+${timestamp}.png`;
    
    // Save image data URL to file
    window.os.fs.write(path, imageDataUrl);
    
    // Notify user of successful save
    window.os.gui.notification(`Snapshot saved to ${path}`);
}

</pre>
