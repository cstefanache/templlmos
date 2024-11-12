## games_minesweper_0
### API

<pre style='text-wrap: wrap'>
function minesweeper() { ... }
            x = Math.floor(Math.random() * 8);
            y = Math.floor(Math.random() * 8);

</pre>
### Instruction

<pre style='text-wrap: wrap'>
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
</pre>
### Output

<pre style='text-wrap: wrap'>
function minesweeper() {
    const root = document.createElement('div');
    root.className = 'gmroot';

    const matrix = Array.from({ length: 8 }, () => Array(8).fill(0));
    const totalMines = 10;
    let score = 64;

    // Place mines and update neighboring cells
    for (let i = 0; i < totalMines; i++) {
        let x, y;
        do {
            x = Math.floor(Math.random() * 8);
            y = Math.floor(Math.random() * 8);
        } while (matrix[x][y] === -40);
        matrix[x][y] = -40;

        for (let dx = -1; dx <= 1; dx++) {
            for (let dy = -1; dy <= 1; dy++) {
                if (dx === 0 && dy === 0) continue;
                const nx = x + dx;
                const ny = y + dy;
                if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8 && matrix[nx][ny] !== -40) {
                    matrix[nx][ny]++;
                }
            }
        }
    }

    const scoreDiv = document.createElement('div');
    scoreDiv.className = 'score';
    scoreDiv.textContent = `Discovered: ${score}`;
    root.appendChild(scoreDiv);

    function reveal(x, y) {
        const cellDiv = document.querySelector(`.cell[data-x="${x}"][data-y="${y}"]`);
        if (cellDiv.classList.contains('visited')) return;

        cellDiv.classList.add('visited');
        cellDiv.textContent = matrix[x][y];

        if (matrix[x][y] < 0) {
            cellDiv.textContent = '💣';
            alert('Game Over', '💣 minesweeper');
        } else {
            score--;
            scoreDiv.textContent = `Discovered: ${score}`;
            if (matrix[x][y] === 0) {
                for (let dx = -1; dx <= 1; dx++) {
                    for (let dy = -1; dy <= 1; dy++) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) {
                            reveal(nx, ny);
                        }
                    }
                }
            }
        }
    }

    for (let i = 0; i < 8; i++) {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';
        for (let j = 0; j < 8; j++) {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell';
            cellDiv.setAttribute('data-x', i);
            cellDiv.setAttribute('data-y', j);
            cellDiv.textContent = ' ';
            cellDiv.addEventListener('click', () => reveal(i, j));
            rowDiv.appendChild(cellDiv);
        }
        root.appendChild(rowDiv);
    }

    return root;
}

</pre>
