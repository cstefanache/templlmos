## osbase_filesystem
### Instruction: 0
<pre style='text-wrap: wrap'>`window.os` function is already defined.
### Instruction:
 Define the following on the `window.os` object under `fs` key:
* `sync()` - save the `filesystem` object to the local storage.
* `readPath(path)` - returns the content of the entry in the `filesystem` object at the given path. path should be split by `/` and the method should traverse the `filesystem` object and return the value at path (allow undefined). if the path starts with `/` remove the leading `/`
* `write(path, content)` - writes the content to an entry in the `filesystem` object at the given path and file name. in the end execute the `sync` method.
* `ls(path) - returns a list of entries in the `filesystem` object at the given path. if path is empty or not found, return the root entries. if the path starts with `/` remove the leading `/`
* `mkdir(path, dirName)` - creates a new directory in the `filesystem` object at the given path and directory name. in the end execute the `sync` method.
* `rm(path)` - removes the object at the given path and file name. in the end execute the `sync` method.
* `isFile(path)` - returns true the entry at the given path is a string. 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here's how you can define these methods on the `window.os` object under the `fs` key:

```javascript
if (!window.os) {
    window.os = {};
}
if (!window.os.fs) {
    window.os.fs = {
        filesystem: {},
        sync: function () {
            window.localStorage.setItem('filesystem', JSON.stringify(this.filesystem));
        },
        readPath: function (path) {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let parts = path.split('/');
            let obj = this.filesystem;
            for (let part of parts) {
                if (obj[part] === undefined) {
                    return undefined;
                } else {
                    obj = obj[part];
                }
            }
            return obj;
        },
        write: function (path, content) {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let parts = path.split('/');
            let obj = this.filesystem;
            for (let i = 0; i < parts.length - 1; i++) {
                if (obj[parts[i]] === undefined) {
                    obj[parts[i]] = {};
                }
                obj = obj[parts[i]];
            }
            obj[parts[parts.length - 1]] = content;
            this.sync();
        },
        ls: function (path = '') {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let obj = this.filesystem;
            if (path !== '') {
                let parts = path.split('/');
                for (let part of parts) {
                    if (obj[part] === undefined) {
                        return undefined;
                    } else {
                        obj = obj[part];
                    }
                }
            }
            return Object.keys(obj);
        },
        mkdir: function (path, dirName) {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let parts = path.split('/');
            let obj = this.filesystem;
            for (let i = 0; i < parts.length - 1; i++) {
                if (obj[parts[i]] === undefined) {
                    obj[parts[i]] = {};
                }
                obj = obj[parts[i]];
            }
            obj[dirName] = {};
            this.sync();
        },
        rm: function (path) {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let parts = path.split('/');
            let obj = this.filesystem;
            let parent = obj;
            for (let i = 0; i < parts.length - 1; i++) {
                if (obj[parts[i]] === undefined) {
                    return;
                } else {
                    parent = obj;
                    obj = obj[parts[i]];
                }
            }
            delete parent[parts[parts.length - 1]];
            this.sync();
        },
        isFile: function (path) {
            if (path[0] === '/') {
                path = path.substring(1);
            }
            let parts = path.split('/');
            let obj = this.filesystem;
            for (let part of parts) {
                if (obj[part] === undefined || typeof obj[part] !== 'string') {
                    return false;
                } else {
                    obj = obj[part];
                }
            }
            return true;
        }
    };
}

```</pre>
### Library
<pre style='text-wrap: wrap'>Here are the methods prefixed with `window.os.fs`:

1. `window.os.fs.sync()` - This method syncs the current state of the file system to localStorage. It converts the file system object to a JSON string and stores it in localStorage under the key 'filesystem'.
2. `window.os.fs.readPath(path)` - This method reads a file or directory at the specified path in the file system. It splits the path into its components, traverses the file system object, and returns the object at the end of the path. If the path does not exist, it returns undefined.
3. `window.os.fs.write(path, content)` - This method writes content to a file at the specified path in the file system. It splits the path into its components, traverses the file system object, and sets the content of the last component to the provided content. It then syncs the file system to localStorage.
4. `window.os.fs.ls(path)` - This method lists the contents of a directory at the specified path in the file system. If no path is provided, it lists the contents of the root directory. It returns an array of the keys of the object at the specified path. If the path does not exist, it returns undefined.
5. `window.os.fs.mkdir(path, dirName)` - This method creates a new directory at the specified path in the file system, given the name of the new directory. It splits the path into its components, traverses the file system object, and creates a new object at the last component of the path, using the provided dirName as the key for this new object. It then syncs the file system to localStorage.
6. `window.os.fs.rm(path)` - This method removes a file or directory at the specified path in the file system. It splits the path into its components, traverses the file system object, and deletes the object at the end of the path. It then syncs the file system to localStorage.
7. `window.os.fs.isFile(path)` - This method checks whether the specified path in the file system points to a file (i.e., it returns true if the path points to a string value in the file system object). If the path does not exist or does not point to a file, it returns false.

Please note that this code assumes that the file system is stored in the localStorage of the browser, so it will not persist across browser sessions or tabs. If you need to persist the file system across these, you would need to implement additional logic to save it to a database or another storage medium.

```</pre>
