## apps_simple-run_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>call register application with 'Run' title, ▶️ as emoji, already defined `application` function reference and 400x70 size</pre>
### Output
<pre style='text-wrap: wrap'>function application(parent) {
    const root = document.createElement('div');
    root.className = 'chat';

    const input = document.createElement('input');
    input.style.width = '100%';
    root.appendChild(input);

    input.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            const instruction = input.value;
            input.value = '';

            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ instruction: instruction, full: false })
            })
            .then(response => response.text())
            .then(scriptContent => {
                const scriptTag = document.createElement('script');
                scriptTag.id = 'run-script';
                scriptTag.textContent = scriptContent;
                document.body.appendChild(scriptTag);
            });
        }
    });

    parent.appendChild(root);
    return root;
}
window.os.registerApplication('Run', '▶️', application, 400, 70);
</pre>
