## apps_run
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 This JavaScript code defines a function `registerApplication` which is used to register an application with certain properties and behaviors in an operating system-like environment. Here's how you can use it:

```javascript
// Assume os and gui objects and registerExtension and addApp methods have been defined elsewhere in your code
// Also assume you have an array of extensions ready to be registered with this application
const extensions = ['ext1', 'ext2', 'ext3']; 

// Define your application's title, emoji, and callback function
const title = 'My App';
const emoji = '🚀';
const callback = (winInstance, param1, param2) => {
  console.log('Callback called with params', param1, param2);
  return 'Some result';  // This will be attached to the window instance and returned from execute function
};

// Register your application with optional parameters for width and height (default is 400)
// and an optional array of extensions (default is undefined)
window.os.registerApplication(title, emoji, callback, 600, 600, extensions); 
```
In this example, `callback` is a function that will be called when your application is executed (i.e., when its icon is clicked in the operating system). It receives two parameters (`param1` and `param2`) which can be any values you choose when calling `execute` (the `execute` function is defined inside `registerApplication` and is called when your application is registered). The `callback` function should return something that will be attached to the window instance and returned from `execute`. 

The `width` and `height` parameters (default is 400) specify the initial size of your application's window when it's first created. 

The `extensions` parameter (default is undefined) is an array of extension names to be registered with your application. Each extension will be registered with your application's `emoji` and `execute` function. 

Finally, `addApp` is called with your application's `emoji`, `title` and `execute` function to add your application to the list of available applications in the operating system. 

This is just an example of how you might use this `registerApplication` function in your code. The actual behavior and requirements of your operating system and its applications would depend on how these methods and objects have been defined elsewhere in your code.

```

 Create an `application` function that takes a parent parameter having the following functionality:
 - create a root dom element with class `chat`
 - create an input element with 100% width with keyup event listener that on enter key press:
   - save the input value to instruction variable and clear the input
   - POST the json having instruction and full as false to `http://localhost:8080`, on response add a script tag to the body with id `run-script` and add the response text content to the script tag
 - return dom element
call register application with 'Run' title, ▶️ as emoji, already defined `application` function reference and 400x70 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can create your `application` function and call `registerApplication` with it. 

```javascript
// Define your application's callback function
const application = (parent) => {
  // Create root DOM element
  const root = document.createElement('div');
  root.className = 'chat';
  parent.appendChild(root);
  
  // Create input element
  const input = document.createElement('input');
  input.style.width = '100%';
  input.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
      // Save input value to instruction variable
      const instruction = event.target.value;
      event.target.value = '';
      
      // POST instruction to server
      fetch('http://localhost:8080', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ instruction: instruction, full: false })
      })
      .then(response => response.text())
      .then(data => {
        // Add script tag to body with response text content
        const script = document.createElement('script');
        script.id = 'run-script';
        script.textContent = data;
        document.body.appendChild(script);
      });
    }
  });
  root.appendChild(input);
  
  return root;
};

// Register your application
window.os.registerApplication('Run', '▶️', application, 400, 70); 

```</pre>
