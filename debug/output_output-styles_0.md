## output_output-styles_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 style .output-wrapper class having a fixed position having top and right to 0 and width 40%  and max-width of 500px and 100% height of the screen
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
    width: 40%;
    max-width: 500px;
    height: 100vh; /* viewport height */
}

.output {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* semi-transparent black */
    color: white; /* white text */
    white-space: pre-wrap; /* text wrap */
    font-size: 9px;
    padding: 10px; /* padding */
    margin: 0; /* no margins */
    overflow: auto; /* scroll if content overflows */
}

</pre>
