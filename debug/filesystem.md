## filesystem

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that holds an empty object called `filesystem` that is loaded from local storage or initialized as empty.
Define the following methods under the global `window.os` object under `fs` key:
* `sync()` - save the `filesystem` object to the local storage.
* `readPath(path)` - returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object to find the content.
* `write(path, fileName, content)` - writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
* `ls(path) - returns a list of entries in the `filesystem` object at the given path. if path is empty or not found, return the root entries. if the path starts with `/` remove the leading `/`
* `mkdir(path, dirName)` - creates a new directory in the `filesystem` object at the given path and directory name. in the end execute the `sync` method.
* `rm(path)` - removes the object at the given path and file name. in the end execute the `sync` method.
* `isFile(path)` - returns true the entry at the given path is a string. 
### Response:

```

```
(function() {
    // Load filesystem from localStorage, if it exists, otherwise initialize it as an empty object
    var filesystem = JSON.parse(localStorage.getItem('filesystem')) || {};
    
    // Define fs methods on window.os
    window.os = window.os || {};
    window.os.fs = {
        sync: function() {
            localStorage.setItem('filesystem', JSON.stringify(filesystem));
        },
        readPath: function(path) {
            var pathArray = path.split('/').filter(Boolean); // Remove leading and trailing '/' and split by '/'
            var current = filesystem;
            for (var i = 0; i < pathArray.length; i++) {
                if (current[pathArray[i]]) {
                    current = current[pathArray[i]];
                } else {
                    return null; // Path not found
                }
            }
            return current; // Return content at path
        },
        write: function(path, fileName, content) {
            var pathArray = path.split('/').filter(Boolean); // Remove leading and trailing '/' and split by '/'
            var current = filesystem;
            for (var i = 0; i < pathArray.length; i++) {
                if (!current[pathArray[i]]) {
                    current[pathArray[i]] = {}; // Create new directory if it doesn't exist
                }
                current = current[pathArray[i]]; // Move to next level in filesystem
            }
            current[fileName] = content; // Write content to file
            this.sync(); // Save filesystem to localStorage
        },
        ls: function(path) {
            var current = path ? this.readPath(path) : filesystem; // Get current directory to list entries in
            return current ? Object.keys(current) : Object.keys(filesystem); // Return entries in current directory
        },
        mkdir: function(path, dirName) {
            var pathArray = path.split('/').filter(Boolean); // Remove leading and trailing '/' and split by '/'
            var current = filesystem;
            for (var i = 0; i < pathArray.length; i++) {
                if (!current[pathArray[i]]) {
                    current[pathArray[i]] = {}; // Create new directory if it doesn't exist
                }
                current = current[pathArray[i]]; // Move to next level in filesystem
            }
            current[dirName] = {}; // Create new directory at given path and name
            this.sync(); // Save filesystem to localStorage
        },
        rm: function(path) {
            var pathArray = path.split('/').filter(Boolean); // Remove leading and trailing '/' and split by '/'
            var parent = filesystem;
            var last = pathArray[pathArray.length - 1]; // Get last part of path (file/directory name)
            pathArray = pathArray.slice(0, -1); // Remove last part of path
            for (var i = 0; i < pathArray.length; i++) {
                if (parent[pathArray[i]]) {
                    parent = parent[pathArray[i]]; // Move to parent directory
                } else {
                    return; // Path not found, nothing to remove
                }
            }
            delete parent[last]; // Remove file/directory at given path
            this.sync(); // Save filesystem to localStorage
        },
        isFile: function(path) {
            var content = this.readPath(path); // Get content at given path
            return typeof content === 'string'; // Return true if content is a string (i.e., it's a file)
        }
    };
})();


```