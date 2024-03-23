## desktop_tests
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The function signature for `window.os.addApp` is as follows:

```javascript
window.os.addApp(emoji, title, callback);

``` 

 call addApp 10 times for 10 different emojis and random titles 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here's a simple way to do it using a loop and some random data generation:

```javascript
// Array of emojis
var emojis = ['😀', '😂', '😍', '😎', '😜', '😀', '😂', '😍', '😎', '😜'];
// Array of titles
var titles = ['Title1', 'Title2', 'Title3', 'Title4', 'Title5', 'Title6', 'Title7', 'Title8', 'Title9', 'Title10'];

// Loop through the arrays
for (var i = 0; i < 10; i++) {
    // Generate a random index within the array bounds
    var randomIndex = Math.floor(Math.random() * emojis.length);
    // Call addApp with the random emoji and title
    window.os.addApp(emojis[randomIndex], titles[randomIndex], function() {
        console.log('Callback called with emoji ' + emojis[randomIndex] + ' and title ' + titles[randomIndex]);
    });
}

```</pre>
