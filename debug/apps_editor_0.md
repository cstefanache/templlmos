## apps_editor_0
### API

<pre style='text-wrap: wrap'>
function editor(win, path) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Create a `editor` function that takes a window and path parameter:
 - create a dom element with class `editor`
 - add a textarea element to the previously created element 100% width and 100% height
 - save reference to the textarea element
 - create toolbar on the `window` parameter
 - if path is not empty, read the file content and set it to the textarea
 - add button to the toolbar with `💾` text save textarea content to the path if path is defined, prompt for the path otherwise
 - return  dom element

call register application with 'Editor' title, ✍️ as emoji, `editor` function reference and 400x450 size for [txt,doc] extensions
</pre>
### Output

<pre style='text-wrap: wrap'>
function editor(win, path) {
    const editorElement = document.createElement('div');
    editorElement.className = 'editor';

    const textarea = document.createElement('textarea');
    textarea.style.width = '100%';
    textarea.style.height = '100%';
    editorElement.appendChild(textarea);

    const toolbar = window.os.gui.createToolbar(win);

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            textarea.value = content;
        }
    }

    toolbar('💾', function() {
        const savePath = path || prompt('Enter the path to save the file:');
        if (savePath) {
            window.os.fs.write(savePath, textarea.value);
        }
    });

    return editorElement;
}

window.os.registerApplication('Editor', '✍️', editor, 400, 450, ['txt', 'doc']);

</pre>
