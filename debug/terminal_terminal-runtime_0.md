## terminal_terminal-runtime_0
### API
<pre style='text-wrap: wrap'>/**
 * Changes the current path to the specified path.
 * @param {string} path - The path to change to.
 */
function cd(path) { ... }
/**
 * Returns the current working directory.
 * @returns {string} - The current path.
 */
function pwd() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>keep a local variable called currentPath with value '/'
define a local function `cd` that takes a string parameter and sets currentPath to it
define a local function `pwd` that returns the parent scope defined currentPath
define and object called bin and referece functions from objects:
 - window.os.fs
 - `cd` and `pwd` functions</pre>
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
</pre>
