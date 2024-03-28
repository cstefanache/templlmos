## apps_chat
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

 Create a `chat` function that takes a parent parameter:
 - create a root dom element with class `chat`
 - create a textarea element with 100% width and 300px height
 - create an input element with 100% width
 - add a button with `📤` text and on click:
   - POST the content of the input to `http://localhost:8080`, on response append the text response to the textarea prefixed with: 'server: '
   - append the content of the input to the textarea prefixed with: 'you: '
   - clear the input

register application with 'Chat' title, 📤 as emoji, chat and 400x400 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can create this chat functionality using pure JavaScript. Note that this example assumes you have access to the Fetch API for making HTTP requests. 

```javascript
function chat(parent) {
  // Create root element
  const chat = document.createElement('div');
  chat.classList.add('chat');
  parent.appendChild(chat);
  
  // Create textarea element
  const textarea = document.createElement('textarea');
  textarea.style.width = '100%';
  textarea.style.height = '300px';
  chat.appendChild(textarea);
  
  // Create input element
  const input = document.createElement('input');
  input.style.width = '100%';
  chat.appendChild(input);
  
  // Create button element
  const button = document.createElement('button');
  button.textContent = '📤';
  button.onclick = () => {
    // Append 'you: ' + input value to textarea
    textarea.value += 'you: ' + input.value + '\n';
    
    // POST input value to server
    fetch('http://localhost:8080', {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain' },
      body: input.value
    })
    .then(response => response.text())
    .then(data => {
      // Append 'server: ' + server response to textarea
      textarea.value += 'server: ' + data + '\n';
      
      // Clear input
      input.value = '';
    });
  };
  chat.appendChild(button);
}

// Register application
window.os.registerApplication('Chat', '📤', chat, 400, 400);

```</pre>
