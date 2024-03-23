## desktop_desktop-app
### API
<pre style='text-wrap: wrap'>The function signature for `window.os.addApp` is as follows:

```javascript
window.os.addApp(emoji, title, callback);

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The method signature for the function `window.os.icon` is as follows:

```javascript
function(parent, emoji, title, callback)

``` 

 Define a function called `addApp` on `window.os` namespace that takes four parameters: emoji, title and a callback:
- call `icon` with element at `#desktop_content`, emoji, title and the callback as parameters 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here's how you can define your `addApp` function on the `window.os` namespace:

```javascript
// Assuming window.os exists and window.os.icon exists
if (!window.os) {
    window.os = {};
}

if (!window.os.addApp) {
    window.os.addApp = function (emoji, title, callback) {
        var parent = document.querySelector('#desktop_content');
        window.os.icon(parent, emoji, title, callback);
    };
}

```</pre>
