## output_output-window_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 crate a root container div element having the class `output-wrapper` and id `output-wrapper`
create and append to root container a pre element having the class `output` and id `output`
create an internal function that fetches the content from 'http://localhost:8080/output' and sets the innerHTML of the output div to the fetched content
calls http://localhost:8080/ping and if the response is 200 then set an interval to call the internal function every 1000ms 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create root container div element
let outputWrapper = document.createElement('div');
outputWrapper.className = 'output-wrapper';
outputWrapper.id = 'output-wrapper';
document.body.appendChild(outputWrapper);

// Create pre element
let output = document.createElement('pre');
output.className = 'output';
output.id = 'output';
outputWrapper.appendChild(output);

// Internal function to fetch content from 'http://localhost:8080/output'
async function fetchContent() {
    try {
        let response = await fetch('http://localhost:8080/output');
        let data = await response.text();
        output.innerHTML = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call http://localhost:8080/ping
fetch('http://localhost:8080/ping')
    .then(response => {
        if (response.status === 200) {
            // If response is 200, set an interval to call fetchContent every 1000ms
            setInterval(fetchContent, 1000);
        } else {
            console.error('Ping failed with status', response.status);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

</pre>
