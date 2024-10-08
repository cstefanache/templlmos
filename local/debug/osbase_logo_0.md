## osbase_logo_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 js that creates an image element with source: https://github.com/cstefanache/templlmos/blob/main/assets/logos.png?raw=true with id #logo, absolute position, middle of the body document, give it 20% opacity 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create a new image element
let img = document.createElement('img');
img.src = 'https://github.com/cstefanache/templlmos/blob/main/assets/logos.png?raw=true?raw=true';
img.id = 'logo';
img.style.position = 'absolute';
img.style.left = '50%';
img.style.top = '50%';
img.style.transform = 'translate(-50%, -50%)'; // To center the image in the middle of its container
img.style.opacity = '0.2'; // Set opacity to 20%

// Append the image to the body of the document
document.body.appendChild(img);

</pre>
