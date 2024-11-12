## terminal_terminal-runtime_1
### API

<pre style='text-wrap: wrap'>
/**
 * Changes the current path to the specified path.
 * @param {string} path - The new path to set as current.
 */
function cd(path) { ... }
/**
 * Returns the current working directory.
 * @returns {string} - The current path.
 */
function pwd() { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
keep a local variable called currentPath with value '/'
define a local function `cd` that takes a string parameter and sets currentPath to it
define a local function `pwd` that returns the parent scope defined currentPath
define and object called bin and referece functions from objects:
 - all window.os.fs functions
 - all window.os.utils functions
 - cd and pwd functions
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

</pre>
