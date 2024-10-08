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
create an internal function fetches the content from '/output' if the data differes from the content: sets the innerHTML of the pre element to the fetched content and  scroll output to bottom
calls /ping and if the response is 200 then set an interval to call the internal function every 1000ms 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create a root container div element with class 'output-wrapper' and id 'output-wrapper'
let rootContainer = document.createElement('div');
rootContainer.className = 'output-wrapper';
rootContainer.id = 'output-wrapper';
document.body.appendChild(rootContainer);

// Create and append to root container a pre element with class 'output' and id 'output'
let output = document.createElement('pre');
output.className = 'output';
output.id = 'output';
rootContainer.appendChild(output);

// Store empty string in a variable 'content'
let content = '';

// Create an internal function fetches the content from '/output' if the data differs from the content
async function fetchContent() {
    let response = await fetch('/output');
    let newContent = await response.text();
    if (newContent !== content) {
        content = newContent;
        output.innerHTML = content; // Set innerHTML of the pre element to the fetched content
        output.scrollTop = output.scrollHeight; // Scroll output to bottom
    }
}

// Call /ping and if the response is 200 then set an interval to call the internal function every 1000ms
fetch('/ping')
    .then(response => {
        if (response.status === 200) {
            setInterval(fetchContent, 1000);
        }
    });

</pre>
