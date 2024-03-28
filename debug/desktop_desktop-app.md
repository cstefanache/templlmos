## desktop_desktop-app
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 window.os = window.os || {}; // If window.os doesn't exist, create it
window.os.addApp = function(emoji, title, callback) {
  window.os.icon(document.querySelector('#desktop_content'), emoji, title, callback);
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>Sure, here is how you can use this `window.os.addApp` function:

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

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:
Given the following examples:
 This JavaScript function creates an icon with an emoji and title and attaches a click event listener to it. The function is stored in `window.os` under the name `icon`. 

Here's how you can use this function:

```javascript
window.os.icon(document.body, '😀', 'Smiling Face', function() {
  console.log('Icon clicked');
});
```
In this example, an icon with an emoji of '😀', title 'Smiling Face', and a callback function that logs 'Icon clicked' when clicked, is created and appended to `document.body`. 

The `parent` parameter is the parent element where you want to append this new icon. The `emoji` parameter is the emoji you want to display in your icon. The `title` parameter is the text you want to display in your icon. The `callback` parameter is a function you want to execute when this icon is clicked. 

This function creates an HTML structure like this: 

```html
<div class="icon">
  <span class="emoji">😀</span>
  <span class="title">Smiling Face</span>
</div>
```
And then attaches an event listener to this `div` element so when you click on this `div`, your callback function will be executed. 

Please note that this function does not return anything (it returns `undefined`), so you cannot assign its result to any variable or use it in any arithmetic expressions or conditions. If you want to use its result (which is `undefined`), you should pass a function as `callback` parameter and handle its result inside this function.

```

 Define a function called `addApp` on `window.os` namespace that takes four parameters: emoji, title and a callback:
- call `icon` with element at `#desktop_content`, emoji, title and the callback as parameters 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can define this `addApp` function on `window.os` namespace:

```javascript
window.os = window.os || {}; // If window.os doesn't exist, create it
window.os.addApp = function(emoji, title, callback) {
  window.os.icon(document.querySelector('#desktop_content'), emoji, title, callback);
};

```</pre>
