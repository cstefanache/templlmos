## games_minesweper_0
### API
<pre style='text-wrap: wrap'>function minesweeper() { ... }
</pre>
### Instruction
<pre style='text-wrap: wrap'>Write only browser JS, JavaScript, HTML and CSS. Document all function declarations using jsdoc.
### Instruction:
Given the following already defined functions:
 /**
 * Register an application on the desktop.
 * 
 * @param {string} title - The tooltip text to display when hovering over this application's icon.
 * @param {string} emoji - The emoji to display in this application's icon.
 * @param {function} callback - The callback to call when this application's icon is clicked.
 * @param {number} [width=400] - The width of the application's window in pixels.
 * @param {number} [height=400] - The height of the application's window in pixels.
 * @param {Array<string>} [extensions] - The file extensions this application can handle.
 */
window.os.registerApplication = function(title, emoji, callback, width = 400, height = 400, extensions) { ... }



 Create a callback function `minesweeper` that:
 - creates a root dom element with the class `gmroot`
 - generate a matrix of 8x8 with values 0
 - pick a random of 10 cells and set their value to -40 and increase the number value of the neighbouring cells
 - set score to 64
 - add a div with the class `score` and the content `Discovered: 64` to the root dom element
 - iterate through the matrix and for each row add a div element with the class `.row` and for each item add a div with the class `cell`,  ` ` as content and add data-x and data-y as attributes. when the div is clicked call `reveal` function for the current x and y
 - define internal function reveal that:
   - get div at x and y using data-x and data-y attributes
   - if the div is already revealed return
   - set the div content to the value of the cell and add class `.visited` to the div
   - if the div has am integer value smaller than 0 set the div content to `💣` and call `alert` with the message `Game Over` and the title `💣 minesweeper`
   - else decrease the score by 1 and update the score div content to `Discovered: ${score}`
   - if the div has an integer value of 0 call `reveal` for all the neighbouring cells
 - return root element 
### Response:
</pre>
### Output
<pre style='text-wrap: wrap'>function minesweeper() {
    // Create root element
    const root = document.createElement('div');
    root.className = 'gmroot';
    
    // Create matrix of size 8x8 with values 0
    const matrix = Array(8).fill().map(() => Array(8).fill(0));
    
    // Pick 10 random cells and set their value to -40 and increase the number value of the neighbouring cells
    let mines = [];
    for (let i = 0; i < 10; i++) {
        let x = Math.floor(Math.random() * 8);
        let y = Math.floor(Math.random() * 8);
        mines.push({x, y});
        matrix[x][y] = -40;
        for (let dx = -1; dx <= 1; dx++) {
            for (let dy = -1; dy <= 1; dy++) {
                if (dx === 0 && dy === 0) continue;
                let nx = x + dx;
                let ny = y + dy;
                if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) matrix[nx][ny]++;
            }
        }
    }
    
    // Set score to 64
    let score = 64;
    
    // Add score div
    const scoreDiv = document.createElement('div');
    scoreDiv.className = 'score';
    scoreDiv.textContent = `Discovered: ${score}`;
    root.appendChild(scoreDiv);
    
    // Add matrix rows
    for (let i = 0; i < 8; i++) {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';
        for (let j = 0; j < 8; j++) {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell';
            cellDiv.textContent = ' ';
            cellDiv.dataset.x = i;
            cellDiv.dataset.y = j;
            cellDiv.addEventListener('click', () => reveal(i, j));
            rowDiv.appendChild(cellDiv);
        }
        root.appendChild(rowDiv);
    }
    
    // Define reveal function
    const reveal = (x, y) => {
        let cellDiv = document.querySelector(`div[data-x="${x}"][data-y="${y}"]`);
        if (cellDiv.classList.contains('visited')) return;
        let value = matrix[x][y];
        cellDiv.textContent = value < 0 ? '💣' : value;
        cellDiv.classList.add('visited');
        if (value < 0) {
            alert('Game Over');
            return;
        } else if (value === 0) {
            for (let dx = -1; dx <= 1; dx++) {
                for (let dy = -1; dy <= 1; dy++) {
                    if (dx === 0 && dy === 0) continue;
                    let nx = x + dx;
                    let ny = y + dy;
                    if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) reveal(nx, ny);
                }
            }
        }
        score--;
        scoreDiv.textContent = `Discovered: ${score}`;
    };
    
    return root;
};

</pre>
