## terminal_terminal-style_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>define a terminal-output class with the following css properties
- flex: 1
- overflow-y: auto
- padding: 10px
- display: flex
- flex-direction: column-reverse</pre>
### Output
<pre style='text-wrap: wrap'>.terminal {
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
</pre>
