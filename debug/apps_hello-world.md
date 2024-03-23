## apps_hello-world
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The method signature of the `registerApplication` function would be as follows:

```javascript
window.os.registerApplication = function(title, emoji, callback, width=400, height=400): void;

``` 

 Create a `helloWorld` function that:
 - creates a root dom element with class `hw`
 - create a new `h1` element with the text `Hello, World!` and appends it to the root element
 - return root dom element
register application with 'hello world' title, 👋 as emoji, `helloWorld` function and 300x200 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is how you can implement this in JavaScript:

```javascript
function helloWorld() {
    // Create a root dom element with class 'hw'
    let rootElement = document.createElement('div');
    rootElement.className = 'hw';
    
    // Create a new 'h1' element with the text 'Hello, World!' and appends it to the root element
    let h1Element = document.createElement('h1');
    h1Element.textContent = 'Hello, World!';
    rootElement.appendChild(h1Element);
    
    // Return root dom element
    return rootElement;
}

// Register application with 'hello world' title, 👋 as emoji, helloWorld function and 300x200 size 
if (typeof window.os !== 'undefined' && typeof window.os.registerApplication === 'function') {
    window.os.registerApplication('hello world', '👋', helloWorld, 300, 200);
} else {
    console.error('The os or registerApplication does not exist');
}

```</pre>
