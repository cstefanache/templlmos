## gui_notification_0
### API
<pre style='text-wrap: wrap'>window.os.gui.notification = function(message) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 crate a root container div element having the class `.notification-wrapper`
Define a function `notification` on the `window.os.gui` object that takes a single parameter message and has the following functionality:
- create a root DOM element with the class `.notification`
- add to the root DOM element a `span` containing the message parameter
- append the root DOM element to .notification-wrapper
- set a timeout of 2000ms to remove the root DOM element from parent 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Firstly, create a root container div element with the class 'notification-wrapper'
let notificationWrapper = document.createElement('div');
notificationWrapper.className = 'notification-wrapper';
document.body.appendChild(notificationWrapper); // Assuming you want to append it to body, but you can change this as per your requirement

// Now define your 'notification' function on 'window.os.gui' object
if (!window.os) { window.os = {}; } // If 'os' object doesn't exist, create it
if (!window.os.gui) { window.os.gui = {}; } // If 'gui' object doesn't exist in 'os', create it
window.os.gui.notification = function(message) {
    // Create a new DOM element with the class 'notification'
    let notificationElement = document.createElement('div');
    notificationElement.className = 'notification';
    
    // Create a 'span' containing the message parameter and append it to 'notification'
    let messageElement = document.createElement('span');
    messageElement.textContent = message; // Set the message as text content of span
    notificationElement.appendChild(messageElement);
    
    // Append 'notification' to '.notification-wrapper'
    notificationWrapper.appendChild(notificationElement);
    
    // Set a timeout of 2000ms to remove 'notification' from parent after 2 seconds
    setTimeout(function() {
        notificationWrapper.removeChild(notificationElement);
    }, 2000);
};

</pre>
