## terminal_terminal-style_5
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
.keyword class has color orange and a right margin of 5px
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
    overflow-wrap: anywhere;
    margin: 0;
    padding: 0;
    min-height: 20px;
}
.terminal-input {
    display: flex;
    flex-direction: row;
}
.terminal-input-text {
    background-color: transparent;
    border: none;
    color: white;
    font-family: monospace;
    font-size: 16px;
    flex: 1;
    outline: none;
}
.keyword {
    color: orange;
    margin-right: 5px;
}

</pre>
