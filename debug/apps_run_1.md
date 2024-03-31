## apps_run_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Register an application on the desktop.
 * 
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 * @param {number} [width=400] - The width of the application's window in pixels.
 * @param {number} [height=400] - The height of the application's window in pixels.
 * @param {Array<string>} [extensions] - The file extensions this application can handle.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) { ... }

/**
 * Create a chat application with a root DOM element and input element.
 * 
 * @param {HTMLElement} parent - The parent element where the chat application will be appended.
 */
function application(parent) { ... }


 call register application with 'Run' title, ▶️ as emoji, already defined `application` function reference and 400x70 size 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>/**
 * Create a chat application with a root DOM element and input element.
 * 
 * @param {HTMLElement} parent - The parent element where the chat application will be appended.
 */
function application(parent) {
    // Create a root DOM element with class 'chat'
    const chat = document.createElement('div');
    chat.className = 'chat';
    parent.appendChild(chat);

    // Create an input element with 100% width
    const input = document.createElement('input');
    input.style.width = '100%';
    chat.appendChild(input);

    // Variable to save input value
    let instruction = '';

    // Event listener for keyup event on input element
    input.addEventListener('keyup', async (event) => {
        // If enter key is pressed
        if (event.key === 'Enter') {
            // Save input value to instruction variable and clear input
            instruction = event.target.value;
            event.target.value = '';
            
            // POST instruction and full as false to 'http://localhost:8080'
            const response = await fetch('http://localhost:8080', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ instruction: instruction, full: false })
            });
            
            // Get response text content
            const content = await response.text();
            
            // Create a script tag with id 'run-script' and add response content to it
            const script = document.createElement('script');
            script.id = 'run-script';
            script.textContent = content;
            document.body.appendChild(script);
        }
    });
    
    // Return root DOM element
    return chat;
}

window.os.registerApplication('Run', '▶️', application, 400, 70);

</pre>
