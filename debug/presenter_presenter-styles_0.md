## presenter_presenter-styles_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers.

.presenter class with 100% width and height, white background, black color, monospace font-family, hidden overflow, flex display and column flex-direction
.presenter .header class with display flex, row flex-direction, 20px height, padding 10px, align-items center and justify-content space-between, yellow background and black color text
.presenter .header img with 100% height
.presenter .header p with margin 0
.presenter .content class with display flex, position realtive, flex 1, padding 10px, overflow hidden, white background
.presenter .footer class with display flex, row-reverse flex-direction,, 20px height, padding 10px, align-items center and justify-content space-between
.presenter .slide should have an absolute position, white background color, 100% width and height, hidden overflow, display flex and column flex-direction
</pre>
### Output
<pre style='text-wrap: wrap'>.presenter {
    width: 100%;
    height: 100%;
    background-color: white;
    color: black;
    font-family: monospace;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.presenter .header {
    display: flex;
    flex-direction: row;
    height: 20px;
    padding: 10px;
    align-items: center;
    justify-content: space-between;
    background-color: yellow;
    color: black;
}

.presenter .header img {
    height: 100%;
}

.presenter .header p {
    margin: 0;
}

.presenter .content {
    display: flex;
    position: relative;
    flex: 1;
    padding: 10px;
    overflow: hidden;
    background-color: white;
}

.presenter .footer {
    display: flex;
    flex-direction: row-reverse;
    height: 20px;
    padding: 10px;
    align-items: center;
    justify-content: space-between;
}

.presenter .slide {
    position: absolute;
    background-color: white;
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
</pre>
