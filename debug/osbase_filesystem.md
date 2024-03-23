## osbase_filesystem
### API
<pre style='text-wrap: wrap'>Sure, here are the method signatures prefixed with `window.os.fs`:

```javascript
// Sync filesystem to localStorage
window.os.fs.sync();

// Read path in filesystem
window.os.fs.readPath(path);

// Write content to path in filesystem and sync it
window.os.fs.write(path, content);

// List entries in path in filesystem
window.os.fs.ls(path);

// Create directory in filesystem and sync it
window.os.fs.mkdir(path, dirName);

// Remove path in filesystem and sync it
window.os.fs.rm(path);

// Check if path in filesystem is a file (i.e., it's a string)
window.os.fs.isFile(path);

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>`window.os` function is already defined.
### Instruction:
 Define the following on the `window.os` object under `fs` key:
loads the `filesystem` object from the local storage.
* `sync()` - save the `filesystem` object to the local storage.
* `readPath(path)` - returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object and return the value at path (allow undefined). if the path starts with `/` remove the leading `/`
* `write(path, content)` - writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
* `ls(path) - returns a list of entries in the `filesystem` object at the given path. if path is empty or not found, return the root entries. if the path starts with `/` remove the leading `/`
* `mkdir(path, dirName)` - creates a new directory in the `filesystem` object at the given path and directory name. in the end execute the `sync` method.
* `rm(path)` - removes the object at the given path and file name. in the end execute the `sync` method.
* `isFile(path)` - returns true the entry at the given path is a string. 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can define these methods in JavaScript, assuming that you have a `filesystem` object in your localStorage:

```javascript
// Check if 'window.os' exists, if not, create it
if (typeof window.os === 'undefined') {
    window.os = {};
}

// Check if 'window.os.fs' exists, if not, create it
if (typeof window.os.fs === 'undefined') {
    window.os.fs = {};
}

// Load filesystem from localStorage if it exists, otherwise initialize it as an empty object
if (localStorage.getItem('filesystem')) {
    window.os.fs.filesystem = JSON.parse(localStorage.getItem('filesystem'));
} else {
    window.os.fs.filesystem = {};
}

// Sync filesystem to localStorage
window.os.fs.sync = function () {
    localStorage.setItem('filesystem', JSON.stringify(this.filesystem));
}

// Read path in filesystem
window.os.fs.readPath = function (path) {
    if (path[0] === '/') {
        path = path.substring(1);
    }
    var pathArray = path.split('/');
    var current = this.filesystem;
    for (var i = 0; i < pathArray.length; i++) {
        if (current[pathArray[i]] === undefined) {
            return undefined;
        } else {
            current = current[pathArray[i]];
        }
    }
    return current;
}

// Write content to path in filesystem and sync it
window.os.fs.write = function (path, content) {
    if (path[0] === '/') {
        path = path.substring(1);
    }
    var pathArray = path.split('/');
    var current = this.filesystem;
    for (var i = 0; i < pathArray.length - 1; i++) {
        if (current[pathArray[i]] === undefined) {
            current[pathArray[i]] = {};
        }
        current = current[pathArray[i]];
    }
    current[pathArray[pathArray.length - 1]] = content;
    this.sync();
}

// List entries in path in filesystem
window.os.fs.ls = function (path) {
    if (path === '') {
        return Object.keys(this.filesystem);
    } else {
        var content = this.readPath(path);
        if (typeof content === 'object') {
            return Object.keys(content);
        } else {
            return [];
        }
    }
}

// Create directory in filesystem and sync it
window.os.fs.mkdir = function (path, dirName) {
    this.write(path + '/' + dirName, {});
}

// Remove path in filesystem and sync it
window.os.fs.rm = function (path) {
    if (path[0] === '/') {
        path = path.substring(1);
    }
    var pathArray = path.split('/');
    var current = this.filesystem;
    for (var i = 0; i < pathArray.length - 1; i++) {
        if (current[pathArray[i]] === undefined) {
            return;
        } else {
            current = current[pathArray[i]];
        }
    }
    delete current[pathArray[pathArray.length - 1]];
    this.sync();
}

// Check if path in filesystem is a file (i.e., it's a string)
window.os.fs.isFile = function (path) {
    var content = this.readPath(path);
    return typeof content === 'string';
}

```</pre>
