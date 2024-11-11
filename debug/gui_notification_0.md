## gui_notification_0
### API
<pre style='text-wrap: wrap'>/**
 * Displays a notification with the given message.
 * @param {string} message - The message to display in the notification.
 */
window.os.gui.notification = function(message) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>crate a root container div element having the class `.notification-wrapper`
Define a function `notification` on the `window.os.gui` object that takes a single parameter message and has the following functionality:
- create a root DOM element with the class `.notification`
- add to the root DOM element a `span` containing the message parameter
- append the root DOM element to .notification-wrapper
- set a timeout of 2000ms to remove the root DOM element from parent</pre>
### Output
<pre style='text-wrap: wrap'>// Create a root container div element with the class .notification-wrapper
const notificationWrapper = document.createElement('div');
notificationWrapper.className = 'notification-wrapper';
document.body.appendChild(notificationWrapper);

/**
 * Displays a notification with the given message.
 * @param {string} message - The message to display in the notification.
 */
window.os = window.os || {};
window.os.gui = window.os.gui || {};
window.os.gui.notification = function(message) {
    const notificationElement = document.createElement('div');
    notificationElement.className = 'notification';
    
    const messageSpan = document.createElement('span');
    messageSpan.textContent = message;
    
    notificationElement.appendChild(messageSpan);
    notificationWrapper.appendChild(notificationElement);
    
    setTimeout(() => {
        notificationElement.remove();
    }, 2000);
};
</pre>
