## apps_browser_1
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>Call register application with 'Browser' title, 📂 as emoji, browser and 450x400 size</pre>
### Output
<pre style='text-wrap: wrap'>function browser(win, path = '') {
    const container = document.createElement('div');
    container.className = 'browser';
    let browserPath = typeof path === 'string' ? path : '';

    function load(path) {
        browserPath = path;
        container.innerHTML = '';

        if (path) {
            const backIcon = document.createElement('div');
            backIcon.className = 'icon';
            const emojiSpan = document.createElement('span');
            emojiSpan.className = 'emoji';
            emojiSpan.textContent = '🔙';
            backIcon.appendChild(emojiSpan);
            backIcon.onclick = () => load(path.split('/').slice(0, -1).join('/'));
            container.appendChild(backIcon);
        }

        const entries = window.os.fs.ls(path);
        entries.forEach(item => {
            const icon = window.os.getOSIcon(path + '/' + item, load);
            container.appendChild(icon);
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = path + '/' + item;
            checkbox.onclick = (e) => e.stopPropagation();
            container.appendChild(checkbox);
        });
    }

    load(browserPath);

    const toolbar = window.os.gui.createToolbar(win);
    toolbar('📁', () => {
        const name = prompt('Enter directory name:');
        if (name) {
            window.os.fs.mkdir(browserPath + '/' + name);
            load(browserPath);
        }
    });
    toolbar('📄', () => {
        const name = prompt('Enter file name:');
        if (name) {
            window.os.fs.write(browserPath + '/' + name, '');
            load(browserPath);
        }
    });
    toolbar('🗑️', () => {
        const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
        checkboxes.forEach(checkbox => {
            window.os.fs.rm(checkbox.value);
        });
        load(browserPath);
    });

    return container;
}
window.os.registerApplication('Browser', '📂', browser, 450, 400);
</pre>
