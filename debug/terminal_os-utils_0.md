## terminal_os-utils_0
### API

<pre style='text-wrap: wrap'>
/**
 * Colorizes JavaScript code within .terminal-line elements by applying different colors
 * to keywords, strings, constants, variables, comments, and functions.
 */
window.os.colorize = function() { ... }
    const stringPattern = /(['"`])(.*?)\1/g;
    const commentPattern = /(\/\/.*?$|\/\*[\s\S]*?\*\/)/gm;
    const functionPattern = /\b\w+(?=\s*\()/g;

</pre>
### Instruction

<pre style='text-wrap: wrap'>
define a function colorize on os that iterates through all .terminal-line elements and color basic js keywords with orange, strings with green, constants and variables in light blue, comments in gray and functions in yellow
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Colorizes JavaScript code within .terminal-line elements by applying different colors
 * to keywords, strings, constants, variables, comments, and functions.
 */
window.os.colorize = function() {
    const terminalLines = document.querySelectorAll('.terminal-line');
    const keywordPattern = /\b(const|let|var|if|else|for|while|function|return|class|new|this|try|catch|throw|async|await|switch|case|break|continue|default|import|export|from|as|instanceof|typeof|void|delete|in|of|with|do|static|extends|super|implements|interface|public|private|protected|readonly|get|set|async|yield|await)\b/g;
    const stringPattern = /(['"`])(.*?)\1/g;
    const commentPattern = /(\/\/.*?$|\/\*[\s\S]*?\*\/)/gm;
    const functionPattern = /\b\w+(?=\s*\()/g;

    terminalLines.forEach(line => {
        let html = line.innerHTML
            .replace(commentPattern, '<span style="color: gray;">$&</span>')
            .replace(stringPattern, '<span style="color: green;">$&</span>')
            .replace(keywordPattern, '<span style="color: orange;">$&</span>')
            .replace(functionPattern, '<span style="color: yellow;">$&</span>');
        
        line.innerHTML = html;
    });
};

</pre>
