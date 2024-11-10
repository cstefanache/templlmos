## desktop_tests_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code.

Given the following implemented functions:
/**
 * Adds an application icon to the desktop with the specified emoji, title, and click callback.
 * @param {string} emoji - The emoji to display in the icon.
 * @param {string} title - The title to display in the icon.
 * @param {Function} callback - The function to call when the icon is clicked.
 */
window.os.addApp = function(emoji, title, callback) { ... }



call addApp 10 times for 10 different emojis and random titles and callback to log the title when clicked
</pre>
### Output
<pre style='text-wrap: wrap'>const emojis = ['😀', '🎉', '🚀', '🌟', '🍕', '🐱', '🏖️', '🎨', '🎮', '📚'];
const titles = ['App One', 'App Two', 'App Three', 'App Four', 'App Five', 'App Six', 'App Seven', 'App Eight', 'App Nine', 'App Ten'];

for (let i = 0; i < 10; i++) {
    window.os.addApp(emojis[i], titles[i], function() {
        console.log(titles[i]);
    });
}
</pre>
