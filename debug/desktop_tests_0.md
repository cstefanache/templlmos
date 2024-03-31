## desktop_tests_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Adds an application to the desktop content. This application is represented as an icon with an emoji and title.
 * @param {string} emoji - The emoji to display in the application's icon.
 * @param {string} title - The title to display in the application's icon.
 * @param {function} callback - The callback to call when the application's icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }



 call addApp 10 times for 10 different emojis and random titles and callback to log the title when clicked 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Array of emojis
var emojis = ['😀', '😂', '😍', '😜', '😎', '😴', '😡', '😱', '😀', '😂'];
// Array of titles
var titles = ['App 1', 'App 2', 'App 3', 'App 4', 'App 5', 'App 6', 'App 7', 'App 8', 'App 9', 'App 10'];

// Loop through each index in the arrays
for (var i = 0; i < emojis.length; i++) {
    // Define a callback that logs the title when called
    var callback = function(title) {
        return function() {
            console.log('Clicked on ' + title);
        };
    }(titles[i]);  // Pass the corresponding title into the callback
    
    // Call addApp with the current index's values
    window.os.addApp(emojis[i], titles[i], callback);
}

</pre>
