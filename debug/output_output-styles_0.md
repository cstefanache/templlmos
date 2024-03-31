## output_output-styles_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 style .output-wrapper class having a fixed position having top and right to 0 and width 300px and 100% height of the screen, z-index of -1
style .output class having:
 - 100% width and height
 - a semi-transparent black background
 - white text
 - text wrap
 - font size of 9px
 - padding of 10px and 0 margins
 - overflow auto 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>.output-wrapper {
    position: fixed;
    top: 0;
    right: 0;
    width: 300px;
    height: 100vh; /* viewport height */
    z-index: -1;
}

.output {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* semi-transparent black */
    color: white; /* white text */
    white-space: pre-wrap; /* text wrap */
    font-size: 9px; /* font size of 9px */
    padding: 10px; /* padding of 10px */
    margin: 0; /* no margins */
    overflow: auto; /* overflow auto */
}

</pre>
