## apps_image_1
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
call register application with 'Image Viewer' title, 🖼️ as emoji, `imageViewer` function reference, 650x520 size for [png,jpg,jpeg] extensions
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Creates an image viewer that displays an image from the specified path.
 * @param {any} unused - Unused parameter.
 * @param {string} path - The path to the image file.
 * @returns {HTMLImageElement} - The image element displaying the image.
 */
function imageViewer(unused, path) {
    const content = window.os.fs.read(path);
    if (!content) {
        throw new Error('File not found or could not be read.');
    }

    const base64Prefix = content.startsWith('data:image/png;base64,') ? 'data:image/png;base64,' : 'data:image/jpeg;base64,';
    const imageContent = content.replace(base64Prefix, '');

    const img = document.createElement('img');
    img.src = 'data:image/png;base64,' + imageContent; // Assuming PNG for simplicity
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.objectFit = 'cover';

    return img;
}

window.os.registerApplication('Image Viewer', '🖼️', imageViewer);
window.os.registerApplication('Image Viewer', '🖼️', imageViewer, 650, 520, ['png', 'jpg', 'jpeg']);

</pre>
