## desktop_icon
### API
<pre style='text-wrap: wrap'>### Instruction:
You are a javascript developer that documents all the declared functions by providing sample usage.
```
 // Check if window.os exists, if not create it
if (!window.os) {
    window.os = {};
}

// Function to create icon
window.os.icon = function(parent, emoji, title, callback) {
    // Create root DOM element with class .icon
    var icon = document.createElement('div');
    icon.className = 'icon';
    
    // Create span with class .emoji and add it to icon
    var emojiSpan = document.createElement('span');
    emojiSpan.className = 'emoji';
    emojiSpan.textContent = emoji;
    icon.appendChild(emojiSpan);
    
    // Create span with class .title and add it to icon
    var titleSpan = document.createElement('span');
    titleSpan.className = 'title';
    titleSpan.textContent = title;
    icon.appendChild(titleSpan);
    
    // Add click event listener to icon
    icon.addEventListener('click', function() {
        // Call the callback when the icon is clicked
        if (callback && typeof(callback) === 'function') {
            callback();
        }
    });
    
    // Add icon to the parent element
    parent.appendChild(icon);
}

 
```
### Response:
</pre>
<pre style='text-wrap: wrap'>This JavaScript function creates an icon with an emoji and title and attaches a click event listener to it. The function is stored in `window.os` under the name `icon`. 

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

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are a frontend web developer, do not use jquery that writes only browser JS, JavaScript, HTML and CSS
### Instruction:


 Define a function called `icon` on `window.os` namespace that takes three parameters: parent, emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `parent`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Here is the code in JavaScript:

```javascript
// Check if window.os exists, if not create it
if (!window.os) {
    window.os = {};
}

// Function to create icon
window.os.icon = function(parent, emoji, title, callback) {
    // Create root DOM element with class .icon
    var icon = document.createElement('div');
    icon.className = 'icon';
    
    // Create span with class .emoji and add it to icon
    var emojiSpan = document.createElement('span');
    emojiSpan.className = 'emoji';
    emojiSpan.textContent = emoji;
    icon.appendChild(emojiSpan);
    
    // Create span with class .title and add it to icon
    var titleSpan = document.createElement('span');
    titleSpan.className = 'title';
    titleSpan.textContent = title;
    icon.appendChild(titleSpan);
    
    // Add click event listener to icon
    icon.addEventListener('click', function() {
        // Call the callback when the icon is clicked
        if (callback && typeof(callback) === 'function') {
            callback();
        }
    });
    
    // Add icon to the parent element
    parent.appendChild(icon);
}

```</pre>
