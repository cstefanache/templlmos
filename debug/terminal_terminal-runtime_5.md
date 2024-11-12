## terminal_terminal-runtime_5
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
call register application with 'Terminal' title, 🖥️ as emoji, terminal function reference and 800x500 size
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
            .replace(/(\b(?:const|let|var|function|return|if|else|for|while|switch|case|break|continue|try|catch|finally|throw|async|await|class|new|this|import|export|from|default|extends|super|static|get|set|void|typeof|instanceof|in|of|with|do|debugger|void|yield|enum|implements|interface|package|private|protected|public|readonly|abstract|declare|namespace|as|assert|any|boolean|never|number|string|symbol|void)\b)/g, '<span style="color: blue;">$1</span>'); // Keywords
        line.innerHTML = html;
    });
}

// Call the function to apply syntax highlighting
colorize();
/**
 * Removes all .terminal-line elements from the document.
 * @function
 */
function clear() {
    const terminalLines = document.querySelectorAll('.terminal-line');
    terminalLines.forEach(line => line.remove());
}
let currentPath = '/';

/**
 * Changes the current path to the specified path.
 * @param {string} path - The new path to set as current.
 */
function cd(path) {
    currentPath = path;
}

/**
 * Returns the current working directory.
 * @returns {string} - The current path.
 */
function pwd() {
    return currentPath;
}

const bin = {
    sync: window.os.fs.sync,
    getPath: window.os.fs.getPath,
    isValidPath: window.os.fs.isValidPath,
    ls: window.os.fs.ls,
    mkdir: window.os.fs.mkdir,
    rm: window.os.fs.rm,
    write: window.os.fs.write,
    read: window.os.fs.read,
    clear: clear,
    colorize: colorize,
    cd: cd,
    pwd: pwd
};
/**
 * Executes a command with the given parameters, processing the path and handling errors.
 * @param {string} input - The command input as a string.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(input) {
    const args = input.match(/(?:[^\s"]+|"[^"]*")+/g);
    let path = currentPath;
    const command = `bin.${args[0]}`;

    if (args[1]) {
        path = args[1].startsWith('/') ? 
            window.os.fs.getPath(args[1]) : 
            window.os.fs.getPath(`${currentPath}/${args[1]}`);
    }

    try {
        return eval(`${command}('${path}'${args.slice(2).map(arg => `, '${arg}'`).join('')})`);
    } catch (error) {
        return error.message;
    }
}
window.apps = window.apps || {};

window.apps.terminal = function() {
    const terminal = document.createElement('div');
    terminal.className = 'terminal';

    const terminalOutput = document.createElement('div');
    terminalOutput.className = 'terminal-output';
    const welcomeLine = document.createElement('pre');
    welcomeLine.className = 'terminal-line';
    welcomeLine.textContent = 'Welcome to TempLLM OS';
    terminalOutput.appendChild(welcomeLine);
    terminal.appendChild(terminalOutput);

    const terminalInput = document.createElement('div');
    terminalInput.className = 'terminal-input';
    const prefix = document.createElement('span');
    prefix.className = 'prefix';
    prefix.textContent = '>';
    const input = document.createElement('input');
    input.className = 'terminal-input-text';
    terminalInput.appendChild(prefix);
    terminalInput.appendChild(input);
    terminal.appendChild(terminalInput);

    function output(value, color = 'white') {
        const line = document.createElement('pre');
        line.className = 'terminal-line';
        line.style.color = color;
        if (Array.isArray(value)) {
            value.forEach(item => {
                const itemLine = document.createElement('pre');
                itemLine.className = 'terminal-line';
                itemLine.style.color = color;
                itemLine.textContent = item;
                terminalOutput.prepend(itemLine);
            });
        } else {
            line.textContent = value;
            terminalOutput.prepend(line);
        }
    }

    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const currentTime = new Date().toLocaleTimeString();
            const content = input.value;
            output(`[${currentTime}] ${content}`, 'yellow');
            const result = execute(content);
            output(result);
            input.value = '';
            input.focus();
        }
    });

    return terminal;
};
window.os.registerApplication('Terminal', '🖥️', window.apps.terminal);

</pre>
