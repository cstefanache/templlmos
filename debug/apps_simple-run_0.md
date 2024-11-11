## apps_simple-run_0
### API
<pre style='text-wrap: wrap'>function application(parent) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Create an `application` function that takes a parent parameter having the following functionality:
 - create a root dom element with class `chat`
 - create an input element with 100% width with keyup event listener that on enter key press:
   - save the input value to instruction variable and clear the input
   - POST the json having instruction and full as false to `/`, on response add a script tag to the body with id `run-script` and add the response text content to the script tag
 - return dom element</pre>
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
</pre>
