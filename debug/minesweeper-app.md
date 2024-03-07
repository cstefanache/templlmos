## minesweeper-app

### Instruction
```
Generate JS code using `let` instead of `var`. All the `os` functions are already defined.
### Instruction:
 Create a self executing function that defines a function called `minesweeper` on the `window.os.apps` object having the following functionality:
* creates a root dom element with the class `gmroot`
* generate a matrix of 8x8 with values 0
* pick a random of 10 cells and set their value to -100 and increase the number value of the neighboring cells
* set score to 64
* add a div with the class `score` and the content `Discovered: 64` to the root dom element
* iterate through the matrix and for each row add a div element with the class `.row` and for each item add a div with the class `cell`,  ` ` as content and add data-x and data-y as attributes. when the div is clicked call `reveal` function for the current x and y
* define internal function reveal that:
  - get div at x and y using data-x and data-y attributes
  - if the div is already revealed return
  - set the div content to the value of the cell and add class `.visited` to the div
  - if the div has am integer value smaller than 0 set the div content to `💣` and call `alert` with the message `Game Over` and the title `💣 minesweeper`
  - else decrease the score by 1 and update the score div content to `Discovered: ${score}`
  - if the div has an integer value of 0 call `reveal` for all the neighboring cells
* call `os.gui.createWindow` with the following parameters: `'💣 minesweeper'`, created root DOM element, `250`, `300` 
### Response:

```

```
(function() {
    window.os = window.os || {};
    window.os.apps = window.os.apps || {};
    
    window.os.apps.minesweeper = function() {
        const root = document.createElement('div');
        root.className = 'gmroot';
        
        const matrix = Array(8).fill().map(() => Array(8).fill(0));
        const bombCoords = [];
        for(let i = 0; i < 10; i++) {
            let x, y;
            do {
                x = Math.floor(Math.random() * 8);
                y = Math.floor(Math.random() * 8);
            } while(bombCoords.find(coord => coord[0] === x && coord[1] === y));
            bombCoords.push([x, y]);
            matrix[x][y] = -100;
            for(let dx = -1; dx <= 1; dx++) {
                for(let dy = -1; dy <= 1; dy++) {
                    if(x + dx >= 0 && x + dx < 8 && y + dy >= 0 && y + dy < 8) {
                        matrix[x + dx][y + dy]++;
                    }
                }
            }
        }
        
        let score = 64;
        const scoreDiv = document.createElement('div');
        scoreDiv.className = 'score';
        scoreDiv.textContent = `Discovered: ${score}`;
        root.appendChild(scoreDiv);
        
        for(let x = 0; x < 8; x++) {
            const rowDiv = document.createElement('div');
            rowDiv.className = 'row';
            for(let y = 0; y < 8; y++) {
                const cellDiv = document.createElement('div');
                cellDiv.className = 'cell';
                cellDiv.textContent = ' ';
                cellDiv.dataset.x = x;
                cellDiv.dataset.y = y;
                cellDiv.addEventListener('click', () => reveal(x, y));
                rowDiv.appendChild(cellDiv);
            }
            root.appendChild(rowDiv);
        }
        
        window.os.gui.createWindow('💣 minesweeper', root, 250, 300);
        
        function reveal(x, y) {
            const cellDiv = document.querySelector(`div[data-x="${x}"][data-y="${y}"]`);
            if(cellDiv.classList.contains('visited')) {
                return;
            }
            cellDiv.classList.add('visited');
            const value = matrix[x][y];
            if(value < 0) {
                cellDiv.textContent = '💣';
                alert('Game Over');
            } else {
                cellDiv.textContent = value;
                score--;
                scoreDiv.textContent = `Discovered: ${score}`;
                if(value === 0) {
                    for(let dx = -1; dx <= 1; dx++) {
                        for(let dy = -1; dy <= 1; dy++) {
                            if(x + dx >= 0 && x + dx < 8 && y + dy >= 0 && y + dy < 8) {
                                reveal(x + dx, y + dy);
                            }
                        }
                    }
                }
            }
        }
    }
})();


```