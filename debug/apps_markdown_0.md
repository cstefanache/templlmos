## apps_markdown_0
### API

<pre style='text-wrap: wrap'>
function markdown(_, path) { ... }
                .replace(/###### (.*)/g, '<h6>$1</h6>')
                .replace(/##### (.*)/g, '<h5>$1</h5>')
                .replace(/#### (.*)/g, '<h4>$1</h4>')
                .replace(/### (.*)/g, '<h3>$1</h3>')
                .replace(/## (.*)/g, '<h2>$1</h2>')
                .replace(/# (.*)/g, '<h1>$1</h1>')
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>')
                .replace(/~~(.*?)~~/g, '<del>$1</del>')
                .replace(/`(.*?)`/g, '<code>$1</code>')

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Create a `markdown` function that takes a _ and path parameter:
 - create a dom element with class `markdown`
 - if path is not empty, read the file content and store it in a variable
 - avoid escaping html code, parse the markdown content and generate html elements for all type of markdown syntax elements and append them to the previously created element
 - return  dom element

call register application with 'markdown' title, 〽️ as emoji, `markdown` function reference and 800x650 size for [md] extensions
</pre>
### Output

<pre style='text-wrap: wrap'>
function markdown(_, path) {
    const markdownElement = document.createElement('div');
    markdownElement.className = 'markdown';

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            const htmlContent = content
                .replace(/###### (.*)/g, '<h6>$1</h6>')
                .replace(/##### (.*)/g, '<h5>$1</h5>')
                .replace(/#### (.*)/g, '<h4>$1</h4>')
                .replace(/### (.*)/g, '<h3>$1</h3>')
                .replace(/## (.*)/g, '<h2>$1</h2>')
                .replace(/# (.*)/g, '<h1>$1</h1>')
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>')
                .replace(/~~(.*?)~~/g, '<del>$1</del>')
                .replace(/`(.*?)`/g, '<code>$1</code>')
                .replace(/\n/g, '<br>');

            markdownElement.innerHTML = htmlContent;
        }
    }

    return markdownElement;
}

window.os.registerApplication('markdown', '〽️', markdown, 800, 650, ['md']);

</pre>
