## development_ide_1
### API

<pre style='text-wrap: wrap'>
function ide(win, path) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
1. Create an `ide` function that takes a win and path parameter: 
 - create a root dom element with class `ide`
 - create a textarea element with 100% width and 500px height
 - if path is not empty, read the file content and set it to the textarea
 - create toolbar on win
 - add button on the toolbar with `▶️` text and on click execute `compile` function with textarea content
 - add button on the toolbar with `💾` text and on click fs.write textarea content to the path if path is defined, prompt for the path otherwise
 - return dom element
2. Call register application with 'IDE' title, 🧠 as emoji, already defined `ide` function reference and 800x600 size and register for ['script'] extensions
</pre>
### Output

<pre style='text-wrap: wrap'>
function compile(source) {
    var existingScript = document.getElementById('run-script');
    if (existingScript) {
        existingScript.remove();
    }

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ instruction: source })
    })
    .then(response => response.text())
    .then(data => {
        var script = document.createElement('script');
        script.id = 'run-script';
        script.textContent = data;
        document.body.appendChild(script);
    })
    .catch(error => console.error('Error:', error));
} // end function
function ide(win, path) {
    const root = document.createElement('div');
    root.className = 'ide';

    const textarea = document.createElement('textarea');
    textarea.style.width = '100%';
    textarea.style.height = '500px';
    root.appendChild(textarea);

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            textarea.value = content;
        }
    }

    const toolbar = window.os.gui.createToolbar(win);
    toolbar('▶️', () => compile(textarea.value));
    toolbar('💾', () => {
        const savePath = path || prompt('Enter path to save:');
        if (savePath) {
            window.os.fs.write(savePath, textarea.value);
        }
    });

    return root;
}

window.os.registerApplication('IDE', '🧠', ide, 800, 600, ['script']);

</pre>
