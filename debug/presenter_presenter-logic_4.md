## presenter_presenter-logic_4
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>call register application with 'Presenter' title, 📽️ as emoji, presenter function reference and 1200x680 size for [xmd] extensions</pre>
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
function readFileContentSync(path) {
    if (window.os.fs.isValidPath(path)) {
        const lines = window.os.fs.read(path);
        if (lines) {
            return lines.join('\n');
        }
    }
    return '';
}
window.apps.presenter = function(_, path = '/itdays.xmd') {
    const rootElement = getPresenterLayout();
    const contentElement = rootElement.querySelector('.content');
    const fileContent = readFileContentSync(path);
    const slides = getSlideDOMElement(fileContent.split('---'));
    
    slides.forEach(slide => contentElement.appendChild(slide));
    
    let currentIndex = 0;
    function showSlide(index) {
        const allSlides = contentElement.children;
        for (let i = 0; i < allSlides.length; i++) {
            allSlides[i].style.display = (i === index) ? 'block' : 'none';
        }
    }
    
    showSlide(currentIndex);
    
    window.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowRight') {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentIndex);
        } else if (event.key === 'ArrowLeft') {
            currentIndex = (currentIndex - 1 + slides.length) % slides.length;
            showSlide(currentIndex);
        }
    });
    
    return rootElement;
};
window.os.registerApplication('Presenter', '📽️', window.apps.presenter, 1200, 680, ['xmd']);
</pre>
