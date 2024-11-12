## terminal_terminal-style_2
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
define a terminal-line class with the following css properties
- display: flex
- flex-direction: row
- margin: 0
- padding: 0
- text-wrap: auto
</pre>
### Output

<pre style='text-wrap: wrap'>
.terminal {
    width: 100%;
    height: 100%;
    background-color: black;
    color: white;
    font-family: monospace;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
.terminal-output {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column-reverse;
}
.terminal-line {
    display: flex;
    flex-direction: row;
    margin: 0;
    padding: 0;
    overflow-wrap: break-word; /* 'text-wrap' is not a valid CSS property */
}

</pre>
