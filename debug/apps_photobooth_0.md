## apps_photobooth_0
### API
<pre style='text-wrap: wrap'>window.photoBooth = function(win) { ... }
reader.onloadend = function() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>create a local photoBooth function that takes a window parameter:
- create a root dom element, do not style it
 - create toolbar on the `window` parameter
- append browser webcam capture video element with autoplay on
- add a button to the toolbar with `📸` text that takes an image snapshot of the video and saves it to 'photobooth/image+{timestamp}.png' and notify the user: 'Snapshot saved to {path}'
- return root dom element</pre>
### Output
<pre style='text-wrap: wrap'>window.photoBooth = function(win) {
    const root = document.createElement('div');
    const toolbar = window.os.gui.createToolbar(win);
    
    const video = document.createElement('video');
    video.autoplay = true;
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Error accessing webcam: ", err);
        });
    
    toolbar('📸', function() {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0);
        
        const timestamp = Date.now();
        const path = `photobooth/image+${timestamp}.png`;
        canvas.toBlob(function(blob) {
            const reader = new FileReader();
            reader.onloadend = function() {
                window.os.fs.write(path, reader.result);
                window.os.gui.notification(`Snapshot saved to ${path}`);
            };
            reader.readAsDataURL(blob);
        });
    });
    
    root.appendChild(video);
    return root;
};
</pre>
