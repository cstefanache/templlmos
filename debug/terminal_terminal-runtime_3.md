## terminal_terminal-runtime_3
### API

<pre style='text-wrap: wrap'>
/**
 * Creates a terminal interface with output and input elements.
 * @returns {HTMLElement} - The terminal root element.
 */
window.apps.terminal = function() { ... }
    /**
     * Outputs a value to the terminal with a specified color.
     * @param {string|Array} value - The value to output.
     * @param {string} [color='white'] - The color of the output text.
     */

</pre>
### Instruction

<pre style='text-wrap: wrap'>
define a function `terminal` on window.apps namespace that creates a root element with class terminal and returns it at the end
create the following dom structure:
 - .terminal
   - .terminal-output
     - .terminal-line with text 'Welcome to TempLLM OS'
   - .terminal-input
     - .prefix with text '>'
     - input.terminal-input-text
define inner function called output that takes two parameters: value and color with default value white. The function prepends a pre with class terminal-line having color style as provided in the function and the value as text to the terminal-output div. if the value is a list then prepend each item in the list as a separate pre
when the user hits the enter key on the input take the content call the output function with the content prefixed with `[%current_time%]` and color yellow, call `output` with the resul of calling `execute` function with the value of the input, clear the input and focus it again and update .prefix text with the currentPath + '>' 
</pre>
### Output

<pre style='text-wrap: wrap'>
/**
 * Removes all elements with the class name 'terminal-line' from the document.
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
    cd: cd,
    pwd: pwd
};
/**
 * Executes a command with the given string input, processing the command and its arguments.
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

/**
 * Creates a terminal interface with output and input elements.
 * @returns {HTMLElement} - The terminal root element.
 */
window.apps.terminal = function() {
    const terminal = document.createElement('div');
    terminal.className = 'terminal';

    const terminalOutput = document.createElement('div');
    terminalOutput.className = 'terminal-output';
    terminal.appendChild(terminalOutput);

    const welcomeMessage = document.createElement('pre');
    welcomeMessage.className = 'terminal-line';
    welcomeMessage.textContent = 'Welcome to TempLLM OS';
    terminalOutput.appendChild(welcomeMessage);

    const terminalInput = document.createElement('div');
    terminalInput.className = 'terminal-input';
    terminal.appendChild(terminalInput);

    const prefix = document.createElement('span');
    prefix.className = 'prefix';
    prefix.textContent = '>';
    terminalInput.appendChild(prefix);

    const inputField = document.createElement('input');
    inputField.className = 'terminal-input-text';
    terminalInput.appendChild(inputField);

    /**
     * Outputs a value to the terminal with a specified color.
     * @param {string|Array} value - The value to output.
     * @param {string} [color='white'] - The color of the output text.
     */
    function output(value, color = 'white') {
        if (Array.isArray(value)) {
            value.forEach(item => {
                const pre = document.createElement('pre');
                pre.className = 'terminal-line';
                pre.style.color = color;
                pre.textContent = item;
                terminalOutput.prepend(pre);
            });
        } else {
            const pre = document.createElement('pre');
            pre.className = 'terminal-line';
            pre.style.color = color;
            pre.textContent = value;
            terminalOutput.prepend(pre);
        }
    }

    inputField.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const currentTime = new Date().toLocaleTimeString();
            const inputValue = inputField.value;
            output(`[${currentTime}] ${inputValue}`, 'yellow');
            const result = execute(inputValue);
            output(result);
            inputField.value = '';
            inputField.focus();
            prefix.textContent = pwd() + '>';
        }
    });

    return terminal;
};

</pre>
