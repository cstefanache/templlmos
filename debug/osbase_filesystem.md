## osbase_filesystem
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Load filesystem object from local storage if it exists
let filesystem = JSON.parse(localStorage.getItem('filesystem')) || {};

// Define window.os.fs object
if (!window.os) { window.os = {}; }
if (!window.os.fs) { window.os.fs = {}; }

// Define sync function
window.os.fs.sync = function() {
    localStorage.setItem('filesystem', JSON.stringify(filesystem));
}

// Define readPath function
window.os.fs.readPath = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length; i++) {
        if (current[pathArray[i]] === undefined) { return undefined; } // path not found
        current = current[pathArray[i]];
    }
    return current;
}

// Define write function
window.os.fs.write = function(path, content) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (file name)
        if (current[pathArray[i]] === undefined) { current[pathArray[i]] = {}; } // create path if it doesn't exist
        current = current[pathArray[i]];
    }
    current[pathArray[pathArray.length - 1]] = content; // set content of file at path
    this.sync(); // save changes to filesystem
}

// Define ls function
window.os.fs.ls = function(path = '') {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let current = this.readPath(path) || filesystem; // get directory at path or root if path is empty or not found
    return Object.keys(current); // return list of entries in directory
}

// Define mkdir function
window.os.fs.mkdir = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (directory name)
        if (current[pathArray[i]] === undefined) { current[pathArray[i]] = {}; } // create path if it doesn't exist
        current = current[pathArray[i]];
    }
    current[pathArray[pathArray.length - 1]] = {}; // create directory at path
    this.sync(); // save changes to filesystem
}

// Define rm function
window.os.fs.rm = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (file name)
        if (current[pathArray[i]] === undefined) { return; } // path not found
        current = current[pathArray[i]];
    }
    delete current[pathArray[pathArray.length - 1]]; // remove file at path
    this.sync(); // save changes to filesystem
}

// Define isFile function
window.os.fs.isFile = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let value = this.readPath(path); // get value at path
    return typeof value === 'string'; // return true if value is string (file)
}

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here is how you can use these functions:

1. `window.os.fs.sync()` - This function will save the current state of your `filesystem` object to `localStorage`. This is useful when you want to persist your data across page reloads or even browser sessions. 

    Example: 
    ```javascript
    window.os.fs.sync();
    ```
2. `window.os.fs.readPath(path)` - This function will read and return the value at a given path in your `filesystem` object. If the path does not exist, it will return `undefined`. 

    Example: 
    ```javascript
    let content = window.os.fs.readPath('/folder/file');
    console.log(content);  // Outputs content of 'file' in 'folder'
    ```
3. `window.os.fs.write(path, content)` - This function will write content to a given path in your `filesystem` object. If the path does not exist, it will create it. 

    Example: 
    ```javascript
    window.os.fs.write('/folder/file', 'Hello, World');
    ```
4. `window.os.fs.ls(path)` - This function will return an array of entries (file names or directory names) in a given directory path. If no path is provided, it will return an array of entries in your root directory (`filesystem`). 

    Example: 
    ```javascript
    let entries = window.os.fs.ls('/folder');
    console.log(entries);  // Outputs array of entries in 'folder'
    ```
5. `window.os.fs.mkdir(path)` - This function will create a directory at a given path in your `filesystem` object. If the path does not exist, it will create it. 

    Example: 
    ```javascript
    window.os.fs.mkdir('/newFolder');
    ```
6. `window.os.fs.rm(path)` - This function will remove an entry (file or directory) at a given path in your `filesystem` object. If the path does not exist, it will do nothing. 

    Example: 
    ```javascript
    window.os.fs.rm('/folder/file');
    ```
7. `window.os.fs.isFile(path)` - This function will return `true` if the given path points to a file (i.e., its value is a string), and `false` otherwise. 

    Example: 
    ```javascript
    let isFile = window.os.fs.isFile('/folder/file');
    console.log(isFile);  // Outputs true if 'file' in 'folder' is a file, false otherwise
    ```
These functions provide a simple file system interface for JavaScript, allowing you to manipulate files and directories in your `filesystem` object using standard file system operations like `read`, `write`, `list`, `create directory`, and `delete`. The `sync` function is used to persist changes to `localStorage`, allowing your data to be saved across page reloads or even browser sessions.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Load the `filesystem` object from the local storage as json
Define the `window.os.fs` object and define the following functions on it:
- Define the `window.os.fs.sync` function that save the `filesystem` object to the local storage.
- Define the `window.os.fs.readPath` function that returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object and return the value at path (allow undefined). if the path starts with `/` remove the leading `/`
- Define the `window.os.fs.write` function that writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
- Define the `window.os.fs.ls` function that returns a list of entries in the `filesystem` object at the given path. if path is empty or not found, return the root entries. if the path starts with `/` remove the leading `/`
- Define the `window.os.fs.mkdir` function that creates a new directory in the `filesystem` object at the given path and directory name. in the end execute the `sync` method.
- Define the `window.os.fs.rm` function that removes the object at the given path and file name. in the end execute the `sync` method.
- Define the `window.os.fs.isFile` function that returns true the entry at the given path is a string. 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can implement these methods in JavaScript:

```javascript
// Load filesystem object from local storage if it exists
let filesystem = JSON.parse(localStorage.getItem('filesystem')) || {};

// Define window.os.fs object
if (!window.os) { window.os = {}; }
if (!window.os.fs) { window.os.fs = {}; }

// Define sync function
window.os.fs.sync = function() {
    localStorage.setItem('filesystem', JSON.stringify(filesystem));
}

// Define readPath function
window.os.fs.readPath = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length; i++) {
        if (current[pathArray[i]] === undefined) { return undefined; } // path not found
        current = current[pathArray[i]];
    }
    return current;
}

// Define write function
window.os.fs.write = function(path, content) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (file name)
        if (current[pathArray[i]] === undefined) { current[pathArray[i]] = {}; } // create path if it doesn't exist
        current = current[pathArray[i]];
    }
    current[pathArray[pathArray.length - 1]] = content; // set content of file at path
    this.sync(); // save changes to filesystem
}

// Define ls function
window.os.fs.ls = function(path = '') {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let current = this.readPath(path) || filesystem; // get directory at path or root if path is empty or not found
    return Object.keys(current); // return list of entries in directory
}

// Define mkdir function
window.os.fs.mkdir = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (directory name)
        if (current[pathArray[i]] === undefined) { current[pathArray[i]] = {}; } // create path if it doesn't exist
        current = current[pathArray[i]];
    }
    current[pathArray[pathArray.length - 1]] = {}; // create directory at path
    this.sync(); // save changes to filesystem
}

// Define rm function
window.os.fs.rm = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let pathArray = path.split('/');
    let current = filesystem;
    for (let i = 0; i < pathArray.length - 1; i++) { // skip last element (file name)
        if (current[pathArray[i]] === undefined) { return; } // path not found
        current = current[pathArray[i]];
    }
    delete current[pathArray[pathArray.length - 1]]; // remove file at path
    this.sync(); // save changes to filesystem
}

// Define isFile function
window.os.fs.isFile = function(path) {
    if (path[0] === '/') { path = path.substring(1); } // remove leading '/' if exists
    let value = this.readPath(path); // get value at path
    return typeof value === 'string'; // return true if value is string (file)
}

```</pre>
