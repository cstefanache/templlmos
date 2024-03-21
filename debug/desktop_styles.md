## desktop_styles
### Instruction: 0
<pre style='text-wrap: wrap'> Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 css style the `.icon` class to match the following rules:
1. 64px width, 64px min height, text-align center, margin of 5px, pointer cursor
2. containing `.emoji` class should be a block, have a font-size of 30px and inline-block display, position relative
3. containing `.title` class should be a block, have a font-size of 8px, monospaced font, black text, padding of 5px, allow word-wrap to break word, black rounded border with white background 
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here is a CSS snippet that matches your requirements:

```css
.icon {
    width: 64px;
    min-height: 64px;
    text-align: center;
    margin: 5px;
    cursor: pointer;
}

.emoji {
    display: inline-block;
    font-size: 30px;
    position: relative;
}

.title {
    display: block;
    font-size: 8px;
    font-family: monospace;
    color: black;
    padding: 5px;
    word-wrap: break-word;
    border: 2px solid black;
    background-color: white;
    border-radius: 5px;
}

```</pre>
