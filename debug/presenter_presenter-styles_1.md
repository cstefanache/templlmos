## presenter_presenter-styles_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>
You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers.

.slide content should be centered with align-items center and justify-content center and text centered
.slide h1 with font-size 5em
.slide h2 with font-size 1.5em
.slide pre with white-space pre-wrap and background-color #201e30, white text, padding 5, margin 0 auto, max-width 720 and text-align left
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
.slide {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.slide h1 {
    font-size: 5em;
}

.slide h2 {
    font-size: 1.5em;
}

.slide pre {
    white-space: pre-wrap;
    background-color: #201e30;
    color: white;
    padding: 5px;
    margin: 0 auto;
    max-width: 720px;
    text-align: left;
}
</pre>
