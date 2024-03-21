## apps_hello-world
### Instruction: 0
<pre style='text-wrap: wrap'>The method signature for the `window.os.application` function is as follows:

```javascript
window.os.application : Function
    Parameters: 
        title : String
        emoji : String
        callback : Function
        width : Number (default 400)
        height : Number (default 400)
    Returns: void

``` Generate browser vanilla JS code without the use of any library or framework. All the `os` functions are already defined.
### Instruction:
 Create a `helloWorld` function that:
 - creates a root dom element with class `hw`
 - create a new `h1` element with the text `Hello, World!` and appends it to the root element
 - return root dom element
create `application` with 'hello world' title, 👋 as emoji, `helloWorld` function and 300x200 size 
### Response:
</pre>
<pre style='text-wrap: wrap'>Here's how you can create a `helloWorld` function and use it with your application:

```javascript
function helloWorld() {
    // Create a root dom element with class 'hw'
    var root = document.createElement('div');
    root.className = 'hw';
    
    // Create a new 'h1' element with the text 'Hello, World!' and append it to the root element
    var h1 = document.createElement('h1');
    h1.textContent = 'Hello, World👋';
    root.appendChild(h1);
    
    // Return root dom element
    return root;
}

// Create application with 'hello world' title, 👋 as emoji, helloWorld function and 300x200 size
window.os.application('hello world', '👋', helloWorld, 300, 200);

```</pre>
