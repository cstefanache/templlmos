## development_ide_0
### API

<pre style='text-wrap: wrap'>
function compile(source) { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Create `compile` function that takes a source parameter and:
 - remove the script tag with id `run-script` if exists
 - fetch post  to `/` with a json having {instruction: source}, and on response create a script tag with id `run-script` and add the response text content to the script tag
 - add end function comment
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

</pre>
