## presenter_presenter-logic_1
### API
<pre style='text-wrap: wrap'>function getPresenterLayout() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>define a function called getPresenterLayout that creates the following dom structure of divs:
 .presenter
   .header
     img[`https://www.itdays.ro/public/images/logo-gri.png`]
     p`INNOVATION, PROGRAMMING AND TECHNOLOGIES`
   .content
   .footer
     img[`https://ascentcore.com/wp-content/uploads/2023/08/AC-Logo.svg`]
and return the .presenter element</pre>
### Output
<pre style='text-wrap: wrap'>function getSlideDOMElement(slides) {
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
function getPresenterLayout() {
    const presenter = document.createElement('div');
    presenter.className = 'presenter';

    const header = document.createElement('div');
    header.className = 'header';

    const headerImage = document.createElement('img');
    headerImage.src = 'https://www.itdays.ro/public/images/logo-gri.png';
    header.appendChild(headerImage);

    const headerText = document.createElement('p');
    headerText.textContent = 'INNOVATION, PROGRAMMING AND TECHNOLOGIES';
    header.appendChild(headerText);

    presenter.appendChild(header);

    const content = document.createElement('div');
    content.className = 'content';
    presenter.appendChild(content);

    const footer = document.createElement('div');
    footer.className = 'footer';

    const footerImage = document.createElement('img');
    footerImage.src = 'https://ascentcore.com/wp-content/uploads/2023/08/AC-Logo.svg';
    footer.appendChild(footerImage);

    presenter.appendChild(footer);

    return presenter;
}
</pre>
