## osbase_outputs_0
### API
<pre style='text-wrap: wrap'></pre>
### Instruction
<pre style='text-wrap: wrap'>call write with the path `/logo.txt` and ascii art of text `TempLLM OS` fill empty spaces with .</pre>
### Output
<pre style='text-wrap: wrap'>const asciiArt = `
TTTTT  EEEEE  M     M  PPPP   L      L       MM     MM     OOO   SSSS
  T    E      MM   MM  P   P  L      L       MMM   MMM    O   O S
  T    EEEE   M M M M  PPPP   L      L       M M M M M    O   O  SSS
  T    E      M     M  P      L      L       M  M  M M    O   O     S
  T    EEEEE  M     M  P      LLLLL  LLLLL   M     M M     OOO  SSSS
`;

const filledAsciiArt = asciiArt.replace(/ /g, '.');

window.os.fs.write('/logo.txt', filledAsciiArt);
</pre>
