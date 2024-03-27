## apps_hello-world
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 This JavaScript code is defining a `registerApplication` function on `window.os` object, which is used to register an application with an operating system. The application is defined by its title, emoji, and a callback function which is called when the application is initialized. The width and height of the application window can also be specified, with default values of 400 if not provided. 

Here is how you can use this code:

```javascript
// Define your emoji, title and callback function
var emoji = '🚀';
var title = 'My App';
var width = 600; 
var height = 400; 
var callback = () => { 
  var rootElement = document.createElement('div'); 
  rootElement.innerHTML = 'Hello, World 🌍'; 
  return rootElement; 
}; 

// Call registerApplication with emoji, title, callback, width and height 
window.os.registerApplication(title, emoji, callback, width, height); 
```
In this example, we define an emoji, title, and width/height for our application, and provide a callback function which creates and returns an HTML element with "Hello, World 🌍" as its content. We then call `registerApplication` with these parameters to register our application with the operating system. 

Please note, this code assumes `window.os` and `window.os.gui` objects exist and `window.os.addApp` method is defined somewhere else in your codebase, as it is not provided in this snippet. 

Also, please note that this code is using ES6 syntax, so it will not work in older browsers unless they support ES6 features. 

This code is also assuming that `window.os` is an object with `gui` and `addApp` methods, and `registerApplication` is a method on `window.os` object which takes title, emoji, callback, width and height as arguments and returns null. 

Please replace `window.os` with actual object and methods if they are different in your codebase.

```

 Create a `helloWorld` function that:
 - creates a root dom element with class `hw`
 - create a new `h1` element with the text `Hello, World!` and appends it to the root element
 - return root dom element
register application with 'hello world' title, 👋 as emoji, `helloWorld` function and 300x200 size 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can create the `helloWorld` function as per your requirements and then register it as an application using your provided snippet as a reference:

```javascript
// Define your emoji, title and callback function
var emoji = '👋';
var title = 'Hello World';
var width = 300; 
var height = 200; 
var callback = () => { 
  var rootElement = document.createElement('div'); 
  rootElement.className = 'hw'; 
  var h1Element = document.createElement('h1'); 
  h1Element.innerText = 'Hello, World!'; 
  rootElement.appendChild(h1Element); 
  return rootElement; 
}; 

// Call registerApplication with emoji, title, callback, width and height 
if(typeof window.os !== 'undefined' && typeof window.os.gui !== 'undefined' && typeof window.os.gui.addApp === 'function') {  // Check if window.os and window.os.gui exist and addApp method exists 
  window.os.gui.addApp(title, emoji, callback, width, height);  // Call addApp method if it exists 
} else {  // If window.os or window.os.gui or addApp method does not exist 
  console.error('The window.os or window.os.gui or addApp method does not exist'); 
} 

```</pre>
