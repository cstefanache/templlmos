## desktop_styles_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 css style the `.icon` class to match the following rules:
1. 64px width, 64px min height, text-align center, margin of 5px, pointer cursor, position relative, display flex with a column flex direction
2. containing `.emoji` class should be a block, have a font-size of 30px and inline-block display, position relative
3. containing `.title` class should be a block, have a font-size of 8px, monospaced font, black text, padding of 5px, allow word-wrap to break word, black rounded border with white background
4. containing `.app-emoji` class should be absolutely positioned  12px on the right of the icon and 20px top
5. containing checkbox should be absolutely positioned  2px on the left of the icon and -6px top 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/* Style for .icon class */
.icon {
    width: 64px;
    min-height: 64px;
    text-align: center;
    margin: 5px;
    cursor: pointer;
    position: relative;
    display: flex;
    flex-direction: column;
}

/* Style for .emoji class */
.emoji {
    display: block;
    font-size: 30px;
    inline-block;
    position: relative;
}

/* Style for .title class */
.title {
    display: block;
    font-size: 8px;
    font-family: monospace;
    color: black;
    padding: 5px;
    word-wrap: break-word;
    border: 2px solid black;
    border-radius: 5px;
    background-color: white;
}

/* Style for .app-emoji class */
.app-emoji {
    position: absolute;
    right: 12px;
    top: 20px;
}

/* Style for checkbox */
input[type="checkbox"] {
    position: absolute;
    left: 2px;
    top: -6px;
}

</pre>
