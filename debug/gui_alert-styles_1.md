## gui_alert-styles_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 css style for a .alert class to follow the following rules:
- white background, a black border of 1px solid
- a black border of 2px solid
- width width of 200px
- word wrap
- padding of 10px
- a border-radius of 5px
- a box-shadow of 2px 2px 0 0 rgba(0,0,0,0.5)
- a top margin of 5px
- a position of relative 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>.alert-wrapper {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.alert {
    background-color: white;
    border: 2px solid black;
    width: 200px;
    word-wrap: break-word;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 2px 2px 0 0 rgba(0,0,0,0.5);
    margin-top: 5px;
    position: relative;
}

</pre>
