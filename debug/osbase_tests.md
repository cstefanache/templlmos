## osbase_tests
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 Sure, here is how you can use these functions:

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

```

 create a new directory in the root directory called `fstest`
create a new file in the `fstest` directory called `test.txt` with the content `hello world`
list the entries in the `fstest` directory and log it to console
read the content of the `fstest/test.txt` file and log it to console
remove the `fstest` directory 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you would accomplish this using the provided file system interface in your question:

```javascript
// Create new directory in root directory called 'fstest'
window.os.fs.mkdir('/fstest');

// Create new file in 'fstest' directory called 'test.txt' with content 'hello world'
window.os.fs.write('/fstest/test.txt', 'hello world');

// List entries in 'fstest' directory and log it to console
let entries = window.os.fs.ls('/fstest');
console.log(entries);  // Outputs array of entries in 'fstest'

// Read content of 'fstest/test.txt' file and log it to console
let content = window.os.fs.readPath('/fstest/test.txt');
console.log(content);  // Outputs 'hello world'

// Remove 'fstest' directory 
window.os.fs.rm('/fstest');

```</pre>
