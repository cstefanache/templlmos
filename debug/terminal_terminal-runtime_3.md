## terminal_terminal-runtime_3
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>call register application with 'Terminal' title, 🖥️ as emoji, terminal function reference and 800x500 size</pre>
### Output
<pre style='text-wrap: wrap'>let currentPath = '/';

/**
 * Changes the current path to the specified path.
 * @param {string} path - The path to change to.
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
    fs: window.os.fs,
    cd: cd,
    pwd: pwd
};
/**
 * Executes a command with the given parameters, processing the input string.
 * @param {string} input - The command input string to execute.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(input) {
    const args = input.match(/(?:[^\s"]+|"[^"]*")+/g).map(arg => arg.replace(/(^"|"$)/g, ''));
    let path = currentPath;
    const command = `bin.${args[0]}`;
    
    if (args[1]) {
        path = args[1].startsWith('/') ? window.os.fs.getPath(args[1]) : window.os.fs.getPath(`${currentPath}/${args[1]}`);
    }
    
    try {
        return eval(`${command}("${path}", ${args.slice(2).map(arg => `"${arg}"`).join(', ')})`);
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
    const welcomeLine = document.createElement('div');
    welcomeLine.className = 'terminal-line';
    welcomeLine.textContent = 'Welcome to TempLLM OS';
    terminalOutput.appendChild(welcomeLine);
    terminal.appendChild(terminalOutput);

    const terminalInput = document.createElement('div');
    terminalInput.className = 'terminal-input';
    const prefix = document.createElement('div');
    prefix.className = 'prefix';
    prefix.textContent = '>';
    const input = document.createElement('input');
    input.className = 'terminal-input-text';
    terminalInput.appendChild(prefix);
    terminalInput.appendChild(input);
    terminal.appendChild(terminalInput);

    function output(value, color = 'white') {
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.style.color = color;
        if (Array.isArray(value)) {
            value.forEach(item => {
                const itemLine = document.createElement('div');
                itemLine.textContent = item;
                itemLine.style.color = color;
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
window.os.registerApplication('Terminal', '🖥️', window.apps.terminal, 800, 500);
</pre>
