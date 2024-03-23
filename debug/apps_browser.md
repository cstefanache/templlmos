## apps_browser
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The method signature of the `registerApplication` function would be as follows:

```javascript
window.os.registerApplication = function(title, emoji, callback, width=400, height=400): void;

```Sure, here are the method signatures prefixed with `window.os.fs`:

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

```The function signatures are as follows:

1. `createToolbar(parent): Object` - This function creates a toolbar in a given parent element and returns an object that has a function to add buttons to the toolbar. The parent parameter should be a DOM element where the toolbar will be appended to.
2. `addButton(text, callback): undefined` - This function adds a button to the toolbar created by `createToolbar()` function. The text parameter should be a string that will be set as the button's text content, and the callback parameter should be a function that will be called when the button is clicked. The function does not return anything, so it returns undefined.

Here's how you can use these methods:

```javascript
var toolbar = window.os.gui.createToolbar(document.body);
toolbar.addButton('Button 1', function() { console.log('Button 1 clicked'); });
toolbar.addButton('Button 2', function() { console.log('Button 2 clicked'); });

``` 

 Create a `browser` function that takes a `parent` parameter:
 - create a root dom element with class `browser`
 - set browserPath variable to `''`
 - generate internal load function that takes path parameter:
   - set browserPath to the path
   - removes all children of the root element
   - if path is not empty, create a new `div` element with text `..` and on click call load with `path.split('/').slice(0, -1).join('/')`
   - lists all files in the path
   - on click, check if the entry isFile and if is false then call load on the new path
 - execute load on browserPath variable
 - create toolbar on the `parent` parameter
 - add button on the toolbar with `📁` text and prompt for a name and call mkdir on current browserPath and provided name
 - add button on the toolbar with `📄` text and prompt for a name and call write on current browserPath and provided name and '' as content
 - return root dom element
exit function definition and register application with 'Browser' title, 📂 as emoji, `browser` function and 400x400 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can implement this in JavaScript:

```javascript
function browser(parent) {
    var browserPath = '';
    var root = document.createElement('div');
    root.className = 'browser';
    parent.appendChild(root);
    
    var load = function(path) {
        browserPath = path;
        while (root.firstChild) {
            root.removeChild(root.firstChild);
        }
        if (browserPath !== '') {
            var upButton = document.createElement('div');
            upButton.textContent = '..';
            upButton.addEventListener('click', function() {load(browserPath.split('/').slice(0, -1).join('/'));});
            root.appendChild(upButton);
        }
        window.os.fs.ls(browserPath).forEach(function(entry) {
            var entryDiv = document.createElement('div');
            entryDiv.textContent = entry;
            entryDiv.addEventListener('click', function() {
                if (!window.os.fs.isFile(browserPath + '/' + entry)) {
                    load(browserPath + '/' + entry);
                }
            });
            root.appendChild(entryDiv);
        });
    };
    load(browserPath);
    
    var toolbar = window.os.gui.createToolbar(parent);
    toolbar.addButton('📁', function() {
        var dirName = prompt('Enter directory name');
        if (dirName) {
            window.os.fs.mkdir(browserPath, dirName);
            load(browserPath);
        }
    });
    toolbar.addButton('📄', function() {
        var fileName = prompt('Enter file name');
        if (fileName) {
            window.os.fs.write(browserPath + '/' + fileName, '');
            load(browserPath);
        }
    });
    
    return root;
}

window.os.registerApplication('Browser', '📂', browser, 400, 400);

```</pre>
