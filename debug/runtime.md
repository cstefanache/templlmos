## runtime

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create async self executing function that holds an empty object called `runtime` initialized as empty.
Define the following methods under the global `window.os` object under `runtime` key:
* await for call `http://localhost:8080/ping` if the response code is 200 set the `runtime` object to `{online: true}` otherwise set it to `{online: false}` on exception set it to `{online: false}` 
### Response:

```

```
(async () => {
    window.os = window.os || {};
    window.os.runtime = {};
    try {
        const response = await fetch('http://localhost:8080/ping');
        if (response.status === 200) {
            window.os.runtime = { online: true };
        } else {
            window.os.runtime = { online: false };
        }
    } catch (error) {
        window.os.runtime = { online: false };
    }
})();


```