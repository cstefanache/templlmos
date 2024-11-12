## terminal_terminal-runtime-colorize_0
### API

<pre style='text-wrap: wrap'>
/**
 * Iterates through all .terminal-line elements and adds colors to JavaScript syntax.
 */
function colorize() { ... }
            .replace(/(\/\/.*?$)/gm, '<span style="color: green;">$1</span>') // Comments
            .replace(/(['"`].*?['"`])/g, '<span style="color: red;">$1</span>') // Strings

</pre>
### Instruction

<pre style='text-wrap: wrap'>
define a function colorize that iterates through all .terminal-line elements and adds colors to js syntax
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Iterates through all .terminal-line elements and adds colors to JavaScript syntax.
 */
function colorize() {
    const terminalLines = document.querySelectorAll('.terminal-line');
    terminalLines.forEach(line => {
        let html = line.innerHTML
            .replace(/(\/\/.*?$)/gm, '<span style="color: green;">$1</span>') // Comments
            .replace(/(['"`].*?['"`])/g, '<span style="color: red;">$1</span>') // Strings
            .replace(/\b(function|const|let|var|if|else|for|while|return|class|new|this|import|export|async|await)\b/g, '<span style="color: blue;">$1</span>') // Keywords
            .replace(/(\b\d+\b)/g, '<span style="color: orange;">$1</span>'); // Numbers
        line.innerHTML = html;
    });
}

// Call the function to apply syntax highlighting
colorize();

</pre>
