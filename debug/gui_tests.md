## gui_tests
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
 The method signature for the `window.os.gui.createWindow` function is as follows:

```javascript
window.os.gui.createWindow : (string, string, function, number, number) => HTMLElement

``` 

 Create window with the title `My Window`, 😃 as emoji and a callback that returns a h1 with text `hello world!` 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>Sure, here's how you can create a window with a title "My Window", emoji "😃", and a callback that returns a h1 with text "hello world!" using your provided method signature:

```javascript
let myCallback = () => {
    let h1 = document.createElement("h1");
    h1.innerText = "hello world!";
    return h1;
}

let myEmoji = "😃";
let myTitle = "My Window";
let myWidth = 500;  // you can adjust these values according to your needs
let myHeight = 300; // you can adjust these values according to your needs

let myElement = window.os.gui.createWindow(myTitle, myEmoji, myCallback, myWidth, myHeight);
document.body.appendChild(myElement); // assuming you want to append it to body

```</pre>
