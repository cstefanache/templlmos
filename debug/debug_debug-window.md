## debug_debug-window
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 create and append to body a pre element having the class `debug` and id `debug`
create an internal function that fetches the content from 'http://localhost:8080/output' and sets the innerHTML of the debug div to the fetched content
calls http://localhost:8080/ping and if the response is 200 then set an interval to call the internal function every 1000ms 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can achieve this using pure JavaScript. 

```javascript
// Create and append to body a pre element having the class 'debug' and id 'debug'
var debugDiv = document.createElement('pre');
debugDiv.id = 'debug';
debugDiv.className = 'debug';
document.body.appendChild(debugDiv);

// Internal function that fetches the content from 'http://localhost:8080/output' 
// and sets the innerHTML of the debug div to the fetched content
function fetchContent() {
    fetch('http://localhost:8080/output')
        .then(response => response.text())
        .then(data => { debugDiv.innerHTML = data; })
        .catch(error => console.error('Error:', error));
}

// Call http://localhost:8080/ping 
fetch('http://localhost:8080/ping')
    .then(response => {
        if (response.status === 200) {
            // If response is 200, set an interval to call the internal function every 1000ms 
            setInterval(fetchContent, 1000);
        } else {
            console.error('Ping failed with status', response.status);
        }
    })
    .catch(error => console.error('Error:', error));

```</pre>
