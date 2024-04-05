## gui_alert_0
### API
<pre style='text-wrap: wrap'>window.os.gui.alert = function(message) { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 

 crate a root container div element having the class `alert-wrapper` and id `alert-wrapper`
Define a function `alert` on the `window.os.gui` object that takes a single parameter message and has the following functionality:
- create a root DOM element with the class `.alert`
- add to the root DOM element a `span` containing the message parameter
- append the root DOM element to #alert-wrapper
- set a timeout of 2000ms to remove the root DOM element from #alert-wrapper 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>// Create alert wrapper if it doesn't exist
if (!document.getElementById('alert-wrapper')) {
    var alertWrapper = document.createElement('div');
    alertWrapper.setAttribute('class', 'alert-wrapper');
    alertWrapper.setAttribute('id', 'alert-wrapper');
    document.body.appendChild(alertWrapper);
}

// Define alert function on window.os.gui object
if (!window.os) { window.os = {}; }
if (!window.os.gui) { window.os.gui = {}; }
window.os.gui.alert = function(message) {
    // Create alert DOM element
    var alert = document.createElement('div');
    alert.setAttribute('class', 'alert');
    
    // Create span DOM element with message as its content
    var alertMessage = document.createElement('span');
    alertMessage.textContent = message;
    
    // Append span to alert
    alert.appendChild(alertMessage);
    
    // Append alert to alert wrapper
    document.getElementById('alert-wrapper').appendChild(alert);
    
    // Set timeout to remove alert after 2000ms
    setTimeout(function() {
        document.getElementById('alert-wrapper').removeChild(alert);
    }, 2000);
};

</pre>
