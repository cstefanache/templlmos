## terminal_terminal-runtime_2
### API

<pre style='text-wrap: wrap'>
/**
 * Executes a command with the given parameters, processing the input string.
 * @param {string} input - The command input string to execute.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(input) { ... }
    const args = input.match(/(?:[^\s"]+|"[^"]*")+/g).map(arg => arg.replace(/(^"|"$)/g, ''));

</pre>
### Instruction

<pre style='text-wrap: wrap'>
currentPath is defined in parent scope
define a function `execute` that takes a string parameter and:
 - splits the string by space but keeps in a single element if it is in quotes
 - set path to currentPath
 - the first element is the command and prepend `bin.` to it
 - if the second element exists:
    - if it does not start with `/`, prepend `currentPath` to it and assign it to path after calling `getPath` on it
    - if it starts with `/`, assign it to path after calling `getPath` on it
 - return eval of `command` with `path` and rest of the parameters from the list as string arguments
 - if the eval throws an error, return the error message
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
 * Returns the current path.
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
        if (!args[1].startsWith('/')) {
            path = window.os.fs.getPath(`${currentPath}/${args[1]}`);
        } else {
            path = window.os.fs.getPath(args[1]);
        }
    }

    try {
        return eval(`${command}("${path}", ${args.slice(2).map(arg => `"${arg}"`).join(', ')})`);
    } catch (error) {
        return error.message;
    }
}

</pre>
