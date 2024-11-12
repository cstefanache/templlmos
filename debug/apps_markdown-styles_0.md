## apps_markdown-styles_0
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
create a .markdown class and style it with common markdown styles
all pre elements in .markdown style it for code display with smaller font and minimal margins and line height for internal p elements
</pre>
### Output

<pre style='text-wrap: wrap'>
.markdown {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

.markdown h1 {
    font-size: 2em;
    margin: 0.67em 0;
}

.markdown h2 {
    font-size: 1.5em;
    margin: 0.83em 0;
}

.markdown h3 {
    font-size: 1.17em;
    margin: 1em 0;
}

.markdown p {
    margin: 1em 0;
}

.markdown ul,
.markdown ol {
    margin: 1em 0;
    padding-left: 2em;
}

.markdown li {
    margin: 0.5em 0;
}

.markdown blockquote {
    margin: 1em 0;
    padding: 0.5em 1em;
    border-left: 4px solid #ccc;
    background-color: #f9f9f9;
}

.markdown pre {
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9em;
    margin: 0.5em 0;
    padding: 1em;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    overflow: auto;
}

.markdown pre p {
    margin: 0;
    line-height: 1.2;
}

</pre>
