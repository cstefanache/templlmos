## registry_extension
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Check if window.os exists, if not create it
if (typeof window.os === 'undefined') {
    window.os = {};
}

// Check if window.os.registry exists, if not create it
if (typeof window.os.registry === 'undefined') {
    window.os.registry = {};
}

// Define registerExtension function
window.os.registerExtension = function(extension, emoji, callback) {
    // Store extension, emoji and callback in window.os.registry
    window.os.registry[extension] = {emoji: emoji, callback: callback};
};

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript code defines a function `registerExtension` in the `window.os.registry` object. This function takes three parameters - `extension`, `emoji` and `callback` - and stores them in `window.os.registry` under the `extension` key. 

Here's how you can use this function:

```javascript
window.os.registerExtension('myExtension', '😄', function(data) {
  console.log('myExtension received data:', data);
});
```
In this example, `'myExtension'` is used as the key to store the `emoji` and `callback` in `window.os.registry`. The `callback` is a function that will be called when some data is passed to this extension. The `data` passed to this function will be logged to the console in this example. 

Please note that this code assumes you have already defined `window.os` and `window.os.registry` in your code somewhere else in your application. If you haven't, you'll need to do so before using `window.os.registerExtension`. 

Also note that this is a very basic example and doesn't handle any potential errors or edge cases in a real-world application. You might want to add error checking and validation to ensure your code behaves correctly under different circumstances.

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 create a new function `registerExtension` on `window.os` object that takes an extension, an emoji and a callback function with the following functionality:
 - stores on the `window.os.registry` object the extension as key and emoji and callback as value 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here is how you can define this in Javascript:

```javascript
// Check if window.os exists, if not create it
if (typeof window.os === 'undefined') {
    window.os = {};
}

// Check if window.os.registry exists, if not create it
if (typeof window.os.registry === 'undefined') {
    window.os.registry = {};
}

// Define registerExtension function
window.os.registerExtension = function(extension, emoji, callback) {
    // Store extension, emoji and callback in window.os.registry
    window.os.registry[extension] = {emoji: emoji, callback: callback};
};

```</pre>
