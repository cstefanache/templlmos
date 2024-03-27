## desktop_tests
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 Sure, here is how you can use this `window.os.addApp` function:

```javascript
// Define your emoji, title and callback function
var emoji = '🚀';
var title = 'My App';
var callback = function() {
  console.log('Callback called');
};

// Call addApp function with emoji, title and callback as arguments
window.os.addApp(emoji, title, callback);
```

In this example, `emoji` is '🚀', `title` is 'My App', and `callback` is an anonymous function that logs 'Callback called'. These values can be replaced with your own values as needed. The `window.os.addApp` function will then use these values to add an application to your desktop. The specifics of how this is done will depend on how your `icon` function is implemented. 

Please note that this is just an example and you may need to adjust this code to fit your specific needs or environment.

```

 call addApp 10 times for 10 different emojis and random titles and callback to log the title when clicked 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, I understand your requirement. Here's an example of how to call `window.os.addApp` 10 times with different emojis, titles, and callbacks:

```javascript
for (let i = 0; i < 10; i++) {
  let emoji = String.fromCodePoint(0x1F300 + i); // This will generate different emojis for each iteration
  let title = `My App ${i+1}`; // This will generate different titles for each iteration
  let callback = function(title) { // This will return a new callback function with the current title
    return function() { 
      console.log(title + ' clicked'); 
    }; 
  }(title); // Call the callback function with the current title
  
  window.os.addApp(emoji, title, callback); // Add the app to the desktop
}

```</pre>
