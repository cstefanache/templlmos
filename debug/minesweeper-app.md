## minesweeper-app

### Instruction
```
Generate JS code using `let` instead of `var`. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that defines a function called `minesweeper` on the `window.os.apps` object having the following functionality:
* creates a root dom element with the class `gmroot`
* generate a matrix of 8x8 with values 0
* pick a random of 3 cells and set their value to `x` and increase the number value of the neighboring cells
* iterate through the matrix and for each row add a div dom element and for each item add a button with the class `cell` and  `.` as content. when the button is clicked, the content should be replaced with the value. when the user clicks on a cell with value `x` replace content with `💣` and notify the user
* call `os.gui.createWindow` with the following parameters: `'💣 minesweeper'`, created root DOM element, `250`, `280` 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.apps = window.os.apps || {};
    
    window.os.apps.minesweeper = function() {
        // create root dom element with class 'gmroot'
        let root = document.createElement('div');
        root.className = 'gmroot';
        document.body.appendChild(root);
        
        // generate matrix of 8x8 with values 0
        let matrix = Array(8).fill().map(() => Array(8).fill(0));
        
        // pick 3 random cells and set their value to 'x' and increase neighboring cells' values
        let mines = Array(3).fill().map(() => [Math.floor(Math.random() * 8), Math.floor(Math.random() * 8)]);
        mines.forEach(([x, y]) => {
            matrix[x][y] = 'x';
            for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    let nx = x + i, ny = y + j;
                    if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8 && matrix[nx][ny] !== 'x') {
                        matrix[nx][ny]++;
                    }
                }
            }
        });
        
        // iterate through matrix and add div and button elements for each cell
        matrix.forEach((row, x) => {
            let div = document.createElement('div');
            row.forEach((value, y) => {
                let button = document.createElement('button');
                button.className = 'cell';
                button.textContent = '.';
                button.onclick = () => {
                    if (matrix[x][y] === 'x') {
                        button.textContent = '💣';
                        alert('You hit a mine 💣');
                    } else {
                        button.textContent = value;
                    }
                };
                div.appendChild(button);
            });
            root.appendChild(div);
        });
        
        // call os.gui.createWindow with parameters '💣 minesweeper', root DOM element, 250, 280
        window.os.gui.createWindow('💣 minesweeper', root, 250, 280);
    };
})();


```