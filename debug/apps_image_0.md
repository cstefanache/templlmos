## apps_image_0
### API

<pre style='text-wrap: wrap'>
/**
 * Creates an image viewer that displays an image from the specified path.
 * @param {any} unused - Unused parameter.
 * @param {string} path - The path to the image file.
 * @returns {HTMLImageElement} - The image element displaying the image.
 */
function imageViewer(unused, path) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Create a local `imageViewer` and generate jsdoc for it function that takes two parameters: `unused` and `path`  with the following functionality:
reads file content as base64 string from the path to a variable `content`
remove data:image/png;base64, or data:image/jpeg;base64 from the content
create image element with src to content
make the image fill the entire parent content
return image element
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

</pre>
