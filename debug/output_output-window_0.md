## output_output-window_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 use browser fetch for API requests
crate a root container div element having the class `output-wrapper` and id `output-wrapper`
create and append to root container a pre element having the class `output` and id `output`
store empty string in a variable `content`
create an internal function fetches the content from 'http://localhost:8080/output' if the data differes from the content: sets the innerHTML of the pre element to the fetched content and  scroll output to bottom
calls http://localhost:8080/ping and if the response is 200 then set an interval to call the internal function every 1000ms 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create root container div element
let rootContainer = document.createElement('div');
rootContainer.className = 'output-wrapper';
rootContainer.id = 'output-wrapper';
document.body.appendChild(rootContainer);

// Create pre element
let output = document.createElement('pre');
output.className = 'output';
output.id = 'output';
rootContainer.appendChild(output);

// Store empty string in content variable
let content = '';

// Internal function to fetch content from 'http://localhost:8080/output'
async function fetchContent() {
    let response = await fetch('http://localhost:8080/output');
    let newContent = await response.text();
    if (newContent !== content) {
        content = newContent;
        output.innerHTML = content;
        output.scrollTop = output.scrollHeight; // Scroll to bottom
    }
}

// Fetch http://localhost:8080/ping
fetch('http://localhost:8080/ping')
    .then(response => {
        if (response.status === 200) {
            // If response is 200, set an interval to call the internal function every 1000ms
            setInterval(fetchContent, 1000);
        }
    });

</pre>
