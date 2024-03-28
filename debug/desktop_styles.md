## desktop_styles
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 css style the `.icon` class to match the following rules:
1. 64px width, 64px min height, text-align center, margin of 5px, pointer cursor, position relative, display flex with a column flex direction
2. containing `.emoji` class should be a block, have a font-size of 30px and inline-block display, position relative
3. containing `.title` class should be a block, have a font-size of 8px, monospaced font, black text, padding of 5px, allow word-wrap to break word, black rounded border with white background
4. containing `.app-emoji` class should be absolutely positioned  12px on the right of the icon and 20px top 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can apply these styles using CSS:

```css
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

.emoji {
    display: block;
    font-size: 30px;
    inline-block;
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

.app-emoji {
    position: absolute;
    right: 12px;
    top: 20px;
}

```</pre>
