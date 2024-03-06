## filesystem

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create a self executing function that holds an empty object called `filesystem` that is loaded from local storage or initialized as empty.
Define the following methods under the global `window.os` object under `fs` key:
* `sync()` - save the `filesystem` object to the local storage.
* `readPath(path)` - returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object and return the value at path (allow undefined). if the path starts with `/` remove the leading `/`
* `write(path, content)` - writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
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
            path = path[0] === '/' ? path.slice(1) : path;  // Remove leading '/' if exists
            var pathArray = path.split('/');
            var current = filesystem;
            for (var i = 0; i < pathArray.length; i++) {
                if (current[pathArray[i]] === undefined) {
                    return undefined;  // Path not found
                } else {
                    current = current[pathArray[i]];  // Traverse down the path
                }
            }
            return current;  // Return content at path
        },
        write: function(path, content) {
            path = path[0] === '/' ? path.slice(1) : path;  // Remove leading '/' if exists
            var pathArray = path.split('/');
            var current = filesystem;
            for (var i = 0; i < pathArray.length - 1; i++) {  // Do not traverse to last element, we will assign content there
                if (current[pathArray[i]] === undefined) {
                    current[pathArray[i]] = {};  // Create path if it does not exist
                }
                current = current[pathArray[i]];  // Traverse down the path
            }
            current[pathArray[pathArray.length - 1]] = content;  // Assign content to last element in path
            this.sync();  // Save filesystem to localStorage
        },
        ls: function(path) {
            path = path[0] === '/' ? path.slice(1) : path;  // Remove leading '/' if exists
            var current = filesystem;
            if (path) {
                var pathArray = path.split('/');
                for (var i = 0; i < pathArray.length; i++) {
                    if (current[pathArray[i]] === undefined) {
                        return undefined;  // Path not found
                    } else {
                        current = current[pathArray[i]];  // Traverse down the path
                    }
                }
            }
            return Object.keys(current);  // Return entries at path
        },
        mkdir: function(path, dirName) {
            this.write(path + '/' + dirName, {});  // Write an empty directory at path
        },
        rm: function(path) {
            path = path[0] === '/' ? path.slice(1) : path;  // Remove leading '/' if exists
            var pathArray = path.split('/');
            var current = filesystem;
            for (var i = 0; i < pathArray.length - 1; i++) {  // Do not traverse to last element, we will remove it here
                if (current[pathArray[i]] === undefined) {
                    return;  // Path not found, do nothing
                } else {
                    current = current[pathArray[i]];  // Traverse down the path
                }
            }
            delete current[pathArray[pathArray.length - 1]];  // Remove last element in path
            this.sync();  // Save filesystem to localStorage
        },
        isFile: function(path) {
            var content = this.readPath(path);
            return typeof content === 'string';  // Return true if content at path is a string
        }
    };
})();


```