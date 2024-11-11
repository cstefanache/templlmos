## registry_hello-world_0
### API
<pre style='text-wrap: wrap'>function helloWorld(parent, path) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Create a `helloWorld` function that takes a parent and path parameter:
 - creates and returns a root element `div` having an h1 child element with 'Hello World' text
 - if path is defined append a pre element containing the content of reading the file at the path
 - returns the root element
after definition, register application with 'hello world' title, 👋 as emoji, `helloWorld` function and 300x200 size</pre>
### Output
<pre style='text-wrap: wrap'>function helloWorld(parent, path) {
    const root = document.createElement('div');
    const heading = document.createElement('h1');
    heading.textContent = 'Hello World';
    root.appendChild(heading);

    if (path) {
        const content = window.os.fs.read(path);
        if (content) {
            const pre = document.createElement('pre');
            pre.textContent = content.join('\n');
            root.appendChild(pre);
        }
    }

    parent.appendChild(root);
    return root;
}

window.os.registerApplication('hello world', '👋', helloWorld, 300, 200);
</pre>
