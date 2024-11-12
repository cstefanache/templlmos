## osbase_fullscreen_0
### API

<pre style='text-wrap: wrap'>
function toggleFullScreen() { ... }

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Create a new function `toggleFullScreen` that toggles the fullscreen mode of the browser
add a span position fixed bottom centered z-index 999999 with a text that says '⌞ ⌝' that when clicked calls the `toggleFullScreen` function
</pre>
### Output

<pre style='text-wrap: wrap'>
function toggleFullScreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

const span = document.createElement('span');
span.textContent = '⌞ ⌝';
span.style.position = 'fixed';
span.style.bottom = '20px';
span.style.left = '50%';
span.style.transform = 'translateX(-50%)';
span.style.zIndex = '999999';
span.style.cursor = 'pointer';
span.onclick = toggleFullScreen;

document.body.appendChild(span);

</pre>
