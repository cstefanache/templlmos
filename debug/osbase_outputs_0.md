## osbase_outputs_0
### API

<pre style='text-wrap: wrap'>

</pre>
### Instruction

<pre style='text-wrap: wrap'>
call write with the path `/logo.txt` and ascii art of text `TempLLM OS` on 10 lines
</pre>
### Output

<pre style='text-wrap: wrap'>
const asciiArt = `
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
T:::::::::::::::::::::T:::::::::::::T
T:::::::::::::::::::::T:::::::::::::T
T:::::TT:::::::TT:::::T:::::::::::::T
TTTTTT  T:::::T  TTTTTT:::::::::::::T
        T:::::T        T:::::::::::::T
        T:::::T        T:::::::::::::T
        T:::::T        T:::::::::::::T
        T:::::T        T:::::::::::::T
        TTTTTTT        TTTTTTTTTTTTTTT
`;

window.os.fs.write('/logo.txt', asciiArt);

</pre>
