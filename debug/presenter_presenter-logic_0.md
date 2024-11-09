## presenter_presenter-logic_0
### API
<pre style='text-wrap: wrap'>function getSlideDOMElement(slides) { ... }
                const altText = line.match(/!\[(.*?)\]/)[1];
                const src = line.match(/\((.*?)\)/)[1];
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



define a function called getSlideDOMElement that takes an array of strings as an argument
iterate the array and for each item:
 split item by `\n`
   iterate the split result and for each line:
     create a slide div element with class slide
     generate html dom elements corresponding to the markdown syntax with headers, text, image and backtick as pre support and append them to the slide element
   append the slide element to the result array
return the result array
</pre>
### Output
<pre style='text-wrap: wrap'>function getSlideDOMElement(slides) {
    const result = [];

    slides.forEach(item => {
        const lines = item.split('\n');
        const slideElement = document.createElement('div');
        slideElement.className = 'slide';

        lines.forEach(line => {
            let element;

            if (line.startsWith('# ')) {
                element = document.createElement('h1');
                element.textContent = line.slice(2);
            } else if (line.startsWith('## ')) {
                element = document.createElement('h2');
                element.textContent = line.slice(3);
            } else if (line.startsWith('### ')) {
                element = document.createElement('h3');
                element.textContent = line.slice(4);
            } else if (line.startsWith('![')) {
                const altText = line.match(/!\[(.*?)\]/)[1];
                const src = line.match(/\((.*?)\)/)[1];
                element = document.createElement('img');
                element.alt = altText;
                element.src = src;
            } else if (line.startsWith('`')) {
                element = document.createElement('pre');
                element.textContent = line.slice(1, -1);
            } else {
                element = document.createElement('p');
                element.textContent = line;
            }

            slideElement.appendChild(element);
        });

        result.push(slideElement);
    });

    return result;
}
</pre>
