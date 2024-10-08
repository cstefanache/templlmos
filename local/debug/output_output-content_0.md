## output_output-content_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 create a root container div element having the class `output-wrapper` and id `output-wrapper`
create and append to root container a pre element having the class `output` and id `output` 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create a new div with class 'output-wrapper' and id 'output-wrapper'
var outputWrapper = document.createElement('div');
outputWrapper.className = 'output-wrapper';
outputWrapper.id = 'output-wrapper';
document.body.appendChild(outputWrapper); // Append it to body or any other parent you want

// Create a new pre with class 'output' and id 'output'
var output = document.createElement('pre');
output.className = 'output';
output.id = 'output';
outputWrapper.appendChild(output); // Append it to outputWrapper

</pre>
