## terminal_terminal-runtime_1
### API
<pre style='text-wrap: wrap'>/**
 * Executes a command with the given parameters, processing the path accordingly.
 * @param {string} commandString - The command string to execute.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(commandString) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.. For each function, provide a brief description of its purpose in jsdoc format.

Given the following implemented functions:
/**
 * Processes and returns a path by taking into account '..', '//' and '/'.
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
 * @param {string} path - The path where to create the object.
 */
window.os.fs.mkdir = function(path) { ... }
/**
 * Removes the object at the given path.
 * @param {string} path - The path of the object to remove.
 */
window.os.fs.rm = function(path) { ... }
/**
 * Writes the content to an entry in the filesystem object at the given path.
 * @param {string} path - The path where to write the content.
 * @param {string} content - The content to write.
 */
window.os.fs.write = function(path, content) { ... }
/**
 * Reads an entry split by '\n' in the filesystem object at the given path.
 * @param {string} path - The path of the file to read.
 * @returns {Array|null} - An array of lines or null if not found.
 */
window.os.fs.read = function(path) { ... }

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


currentPath is defined in parent scope
define a function `execute` that takes a string parameter and:
 - splits the string by space
 - set path to currentPath
 - the first element is the command and prepend `bin.` to it
 - if the second element exists:
    - if it does not start with `/`, prepend `currentPath` to it and assign it to path after calling `getPath` on it
    - if it starts with `/`, assign it to path after calling `getPath` on it
 - return eval of `command` with `path` and rest of the parameters from the list as arguments
 - if the eval throws an error, return the error message
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
 * Executes a command with the given parameters, processing the path accordingly.
 * @param {string} commandString - The command string to execute.
 * @returns {any} - The result of the command execution or an error message.
 */
function execute(commandString) {
    const args = commandString.split(' ');
    let path = currentPath;
    const command = 'bin.' + args[0];

    if (args[1]) {
        if (!args[1].startsWith('/')) {
            path = window.os.fs.getPath(currentPath + '/' + args[1]);
        } else {
            path = window.os.fs.getPath(args[1]);
        }
    }

    try {
        return eval(`${command}('${path}'${args.slice(2).map(arg => `, '${arg}'`).join('')})`);
    } catch (error) {
        return error.message;
    }
}
</pre>