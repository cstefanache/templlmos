## games_styles_0
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
css style for a .gmroot class to follow the following rules:
- `.gmroot` is a flex container with column direction, centered content, margin of 2px, padding of 4px, background color of white
- `.row` is display flex with row direction, centered content
- `.cell` classes in `.gmroot` be the size of 22px by 22px, inline flex with content centered vertically and horizontally, 2px rounded dark grey border 1px width, margin of 1px, monospace font
- `.cell.visited` class to have a background color of white, 1px white border
- `.score` class to have a margin of 4px, monospace font, bold, centered text, background color of white, 2px rounded white border
</pre>
### Output

<pre style='text-wrap: wrap'>
.gmroot {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 2px;
    padding: 4px;
    background-color: white;
}

.row {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.cell {
    width: 22px;
    height: 22px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    border: 1px solid darkgrey;
    border-radius: 2px;
    margin: 1px;
    font-family: monospace;
}

.cell.visited {
    background-color: white;
    border: 1px solid white;
}

.score {
    margin: 4px;
    font-family: monospace;
    font-weight: bold;
    text-align: center;
    background-color: white;
    border: 2px solid white;
    border-radius: 2px;
}

</pre>
