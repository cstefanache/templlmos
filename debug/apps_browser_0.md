## apps_browser_0
### API
<pre style='text-wrap: wrap'>function browser(win, path = '') { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>1. Create a `browser` function that takes a win and path defaulting to '' parameter:
 - create a container dom element with class `browser`
 - set browserPath to path or `''` if path is undefined or not string
 - generate internal load function that takes path parameter:
   - set browserPath to path
   - removes all children of the container element
   - if path is not empty, create a new `div` with class icon, inner element `.emoji` with internal span element having content '🔙'  and class `emoji` and on click call load with `path.split('/').slice(0, -1).join('/')`
   - ls all files in the path and for each item:
      - call `getOsIcon` with path+'/'+item and load function as callback
      - add a checkbox with value path+'/'+item that prevent event bubbling
 - execute load on browserPath variable
 - create toolbar
 - call `addButton` on the toolbar with `📁` text and prompt for a name and call mkdir on current browserPath and provided name
 - call `addButton` on the toolbar with `📄` text and prompt for a name and call write on current browserPath and provided name and '' as content
 - call `addButton` on the toolbar with `🗑️` text and list all the selected checkbox values, removes them and calls load on the current path
 - return dom element</pre>
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
</pre>
