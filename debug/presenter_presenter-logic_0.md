## presenter_presenter-logic_0
### API

<pre style='text-wrap: wrap'>
function getSlideDOMElement(slides) { ... }
                    const altText = line.match(/!\[(.*?)\]/)[1];
                    const src = line.match(/\((.*?)\)/)[1];

</pre>
### Instruction

<pre style='text-wrap: wrap'>
define a function called getSlideDOMElement that takes an array of strings as an argument
iterate the array and for each item:
 split item by `\n`
   iterate the split result and for each line:
     if the line starts with a dot and a string append the class of the slide to the string
     create a slide div element with class slide
     generate html dom elements corresponding to the markdown syntax with headers, text, image and backtick as pre support and append them to the slide element
   append the slide element to the result array
return the result array
</pre>
### Output

<pre style='text-wrap: wrap'>
function getSlideDOMElement(slides) {
    const result = [];
    slides.forEach(item => {
        const lines = item.split('\n');
        const slideElement = document.createElement('div');
        slideElement.className = 'slide';

        lines.forEach(line => {
            if (line.startsWith('.')) {
                slideElement.classList.add(line.substring(1).trim());
            } else {
                let element;
                if (line.startsWith('# ')) {
                    element = document.createElement('h1');
                    element.textContent = line.substring(2).trim();
                } else if (line.startsWith('## ')) {
                    element = document.createElement('h2');
                    element.textContent = line.substring(3).trim();
                } else if (line.startsWith('### ')) {
                    element = document.createElement('h3');
                    element.textContent = line.substring(4).trim();
                } else if (line.startsWith('![')) {
                    const altText = line.match(/!\[(.*?)\]/)[1];
                    const src = line.match(/\((.*?)\)/)[1];
                    element = document.createElement('img');
                    element.src = src;
                    element.alt = altText;
                } else if (line.startsWith('`')) {
                    element = document.createElement('pre');
                    element.textContent = line.substring(1, line.length - 1).trim();
                } else {
                    element = document.createElement('p');
                    element.textContent = line.trim();
                }
                slideElement.appendChild(element);
            }
        });

        result.push(slideElement);
    });
    return result;
}

</pre>
