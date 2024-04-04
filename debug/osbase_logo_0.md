## osbase_logo_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 js that creates an image element with source: https://ascentcore.com/wp-content/uploads/2023/08/AC-Logo.svg with id #logo, absolute position, middle of the document 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create a new image element
var img = document.createElement('img');
img.src = 'https://ascentcore.com/wp-content/uploads/2023/08/AC-Logo.svg';
img.id = 'logo';
img.style.position = 'absolute';
img.style.left = '50%';
img.style.top = '50%';
img.style.transform = 'translate(-50%, -50%)'; // This will center the image in both x and y axis

// Append the image to the body of your document
document.body.appendChild(img);

</pre>
