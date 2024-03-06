## fs-structure

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 add to local storage the following json {"temp":{"hello world.txt":"Hello World!"}} at the `filesystem` key 
### Response:

```

```
var files = { "temp": { "hello_world.txt": "Hello World!" } };
localStorage.setItem('filesystem', JSON.stringify(files));


```