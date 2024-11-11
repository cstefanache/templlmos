## apps_photobooth_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>call register application with 'Photobooth' title, 📸 as emoji, function reference and 410x360 size</pre>
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
window.os.registerApplication('Photobooth', '📸', window.photoBooth, 410, 360);
</pre>
