## apps_markdown_0
### API
<pre style='text-wrap: wrap'>function markdown(_, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Create a `markdown` function that takes a _ and path parameter:
 - create a dom element with class `markdown`
 - if path is not empty, read the file content and store it in a variable
 - avoid escaping html code, parse the markdown content and generate html elements for all type of markdown syntax elements and append them to the previously created element
 - return  dom element

call register application with 'markdown' title, 〽️ as emoji, `markdown` function reference and 800x650 size for [md] extensions</pre>
### Output
<pre style='text-wrap: wrap'>function markdown(_, path) {
    const markdownElement = document.createElement('div');
    markdownElement.className = 'markdown';

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            const htmlContent = content.map(line => {
                if (line.startsWith('# ')) {
                    return `<h1>${line.slice(2)}</h1>`;
                } else if (line.startsWith('## ')) {
                    return `<h2>${line.slice(3)}</h2>`;
                } else if (line.startsWith('### ')) {
                    return `<h3>${line.slice(4)}</h3>`;
                } else if (line.startsWith('- ')) {
                    return `<li>${line.slice(2)}</li>`;
                } else {
                    return `<p>${line}</p>`;
                }
            }).join('');
            markdownElement.innerHTML = htmlContent;
        }
    }

    return markdownElement;
}

window.os.registerApplication('markdown', '〽️', markdown, 800, 650, ['md']);
</pre>
