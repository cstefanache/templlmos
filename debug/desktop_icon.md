## desktop_icon
### API
<pre style='text-wrap: wrap'>The method signature for the function `window.os.icon` is as follows:

```javascript
function(parent, emoji, title, callback)

```</pre>
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 Define a function called `icon` on `window.os` namespace that takes three parameters: parent, emoji, title and a callback:
- create a root DOM element with the class `.icon` and add it to `parent`
- add a span with the class `.emoji` and the emoji as its content
- add a span with the class `.title` and the title as its content
- when the icon is clicked, call the callback 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here is how you can define this function in JavaScript:

```javascript
// Check if window.os exists, if not create it
if (!window.os) {
    window.os = {};
}

// Function to add icon to parent
window.os.icon = function(parent, emoji, title, callback) {
    // Create root DOM element
    var icon = document.createElement('div');
    icon.classList.add('icon');
    
    // Create span for emoji
    var emojiSpan = document.createElement('span');
    emojiSpan.classList.add('emoji');
    emojiSpan.textContent = emoji;
    
    // Create span for title
    var titleSpan = document.createElement('span');
    titleSpan.classList.add('title');
    titleSpan.textContent = title;
    
    // Append spans to icon
    icon.appendChild(emojiSpan);
    icon.appendChild(titleSpan);
    
    // Append icon to parent
    parent.appendChild(icon);
    
    // Add click event listener to icon
    icon.addEventListener('click', function() {
        // Callback when icon is clicked
        if (typeof callback === 'function') {
            callback();
        }
    });
};

```</pre>
