## terminal_terminal-runtime_2
### API
<pre style='text-wrap: wrap'>window.apps.terminal = function() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Given the following implemented functions:
    /**
     * Saves the filesystem object to local storage.
     * @function
     */
window.os.fs.sync = function() { ... }
    /**
     * Processes and returns a path, handling '..', '//' and '/'.
     * @param {string} path - The path to process.
     * @returns {string|null} - The processed path or null if invalid.
     */
window.os.fs.getPath = function(path) { ... }
    /**
     * Checks if the path is valid.
     * @param {string} path - The path to check.
     * @returns {boolean} - True if valid, false otherwise.
     */
window.os.fs.isValidPath = function(path) { ... }
    /**
     * Returns a list of entries in the filesystem object at the given path.
     * @param {string} path - The path to list entries from.
     * @returns {Array} - An array of entries.
     */
window.os.fs.ls = function(path) { ... }
    /**
     * Creates an empty object at the given path.
     * @param {string} path - The path to create the directory at.
     */
window.os.fs.mkdir = function(path) { ... }
    /**
     * Removes the object at the given path.
     * @param {string} path - The path to remove the object from.
     */
window.os.fs.rm = function(path) { ... }
    /**
     * Writes the content to an entry in the filesystem object at the given path.
     * @param {string} path - The path to write to.
     * @param {string} content - The content to write.
     */
window.os.fs.write = function(path, content) { ... }
    /**
     * Reads an entry split by '\n' in the filesystem object at the given path.
     * @param {string} path - The path to read from.
     * @returns {Array|null} - An array of lines or null if not found.
     */
window.os.fs.read = function(path) { ... }

/**
 * Registers a new application with a title, emoji, callback, dimensions, and optional extensions.
 * @param {string} title - The title of the application.
 * @param {string} emoji - The emoji to display for the application.
 * @param {Function} callback - The function to call when the application is executed.
 * @param {number} [width=400] - The width of the application window.
 * @param {number} [height=400] - The height of the application window.
 * @param {Array} [extensions=undefined] - An optional array of extensions to register with the application.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions = undefined) { ... }

/**
 * Changes the current path to the specified path.
 * @param {string} path - The path to change to.
 */
function cd(path) { ... }
/**
 * Returns the current working directory.
 * @returns {string} - The current path.
 */
function pwd() { ... }
/**
 * Executes a command with the given parameters, processing the input string.
 * @param {string} input - The command input string to execute.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(input) { ... }
    const args = input.match(/(?:[^\s"]+|"[^"]*")+/g).map(arg => arg.replace(/(^"|"$)/g, ''));


define a function `terminal` on window.apps that creates a root element with class terminal and returns it at the end
create the following dom structure:
 - .terminal
   - .terminal-output
     - .terminal-line with text 'Welcome to TempLLM OS'
   - .terminal-input
     - .prefix with text '>'
     - input.terminal-input-text
define inner function called output that takes two parameters: value and color with default value white. The function prepends a div with class terminal-line having color style as provided in the function and the value as text to the terminal-output div. if the value is a list then prepend each item in the list as a separate div
when the user hits the enter key on the input take the content call the output function with the content prefixed with `[%current_time%]` and color yellow, call `output` with the resul of calling `execute` function with the value of the input, clear the input and focus it again
</pre>
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
        return eval(`${command}('${path}', ${args.slice(2).map(arg => `'${arg}'`).join(', ')})`);
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
        if (Array.isArray(value)) {
            value.forEach(item => {
                const line = document.createElement('div');
                line.className = 'terminal-line';
                line.style.color = color;
                line.textContent = item;
                terminalOutput.prepend(line);
            });
        } else {
            const line = document.createElement('div');
            line.className = 'terminal-line';
            line.style.color = color;
            line.textContent = value;
            terminalOutput.prepend(line);
        }
    }

    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const content = input.value;
            const currentTime = new Date().toLocaleTimeString();
            output(`[${currentTime}] ${content}`, 'yellow');
            const result = execute(content);
            output(result);
            input.value = '';
            input.focus();
        }
    });

    return terminal;
};
</pre>
