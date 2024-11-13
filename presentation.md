# Personalization
---
.dark
# kernel panic!
---
# LLMs: A Paradigm Shift in Operating Systems
![image](https://avatars.githubusercontent.com/u/3071201?s=96&v=4)
## cornel stefanache
### cto@ascentcore
### co-creator@monkeyuser.com
---
.dark
![image](https://github.com/cstefanache/templlmos/blob/main/images/inspiration.png?raw=true)
---
# Can LLM Write Good OS Code?
---
# Can LLM Write OS Code?
---
# Can LLM Write OS?
---
# What to expect
![image](https://github.com/cstefanache/templlmos/blob/main/images/code-1.png?raw=true)
---
# What to expect
![image](https://github.com/cstefanache/templlmos/blob/main/images/code-2.png?raw=true)
---
# What to expect
![image](https://github.com/cstefanache/templlmos/blob/main/images/code-3.png?raw=true)
---
# What to expect
![image](https://github.com/cstefanache/templlmos/blob/main/images/mistakes.png?raw=true)
---
# The first problem
### Storage
![image](https://github.com/cstefanache/templlmos/blob/main/images/fs-1.png?raw=true)
---
# The second problem
### No file concept
![image](https://github.com/cstefanache/templlmos/blob/main/images/fs-2.png?raw=true)
---
# The third problem
### Interract
![image](https://github.com/cstefanache/templlmos/blob/main/images/fs-3.png?raw=true)
---
# Filesystem
`Define the following functions on the window.os.fs object:`
`  sync - save the filesystem object to the local storage that will be called by the other functions that modify the filesystem object`
`  getPath - process and return a path by taking into account "..", "//" and "/"". return null if the path is invalid`
`  isValidPath - checks if the path is valid`
`  ls - returns a list of entries in the filesystem object at the given path`
`  mkdir - creates an empty object at the given path`
`  rm - removes the object at the given path`
`  write - writes the content to an entry in the filesystem object at the given path`
`  read - reads an entry split by \\n in the filesystem object at the given path, last element in path is the file name`
---
# Under the hood

`<SYSTEM>`
`<DEPENDENCIES>`
`<INSTRUCTION>`
---
# Under the hood - CSS
## System Prompt
`You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers.`
---
# Under the hood - JS
## System Prompt
`You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.`

`if isLibrary == True:`
`    system_prompt += ". For each function, provide a brief description of its purpose in jsdoc format."`
---
# Generated JSDOC
`    /**`
`     * Returns a list of entries in the filesystem object at the given path.`
`     * @param {string} path - The path to list entries from.`
`     * @returns {Array} - An array of entries.`
`     */`
`    window.os.fs.ls = function(path) { ... }`
`    /**`
`     * Creates an empty object at the given path.`
`     * @param {string} path - The path to create the directory.`
`     */`
`    window.os.fs.mkdir = function(path) { ... }`
`    /**`
`     * Removes the object at the given path.`
`     * @param {string} path - The path to remove the object from.`
`     */`
`    window.os.fs.rm = function(path) { ... }`