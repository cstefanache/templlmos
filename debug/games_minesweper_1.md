## games_minesweper_1
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
Call register application with 'Minesweeper' title, 💣 as emoji, `minesweeper` callback function reference and 300x300 size
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
window.os.registerApplication('Minesweeper', '💣', minesweeper, 300, 300);

</pre>
