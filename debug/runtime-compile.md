## runtime-compile

### Instruction
```
Generate browser vanilla JS code without the use of any library or framework.
### Instruction:
 Create async self executing function that:
Define a function on the global `window.os.runtime` under the `compile` key having a single parameter `code` that:
* await for POST call `http://localhost:8080/compile` with a json body `{"model": "deepseek-coder-6.7b-instruct.Q5_K_M.gguf", instruction: code}`
* read the resulted text from the response and store it in a variable called `result`
* search the script element with ID `dev` and if it exists remove it
* create a new script element with ID `dev` and set its inner text to the `result`
* return result 
### Response:

```

```
// Define the function on window.os.runtime under compile key
window.os.runtime = window.os.runtime || {};
window.os.runtime.compile = async (code) => {
    // Make an asynchronous POST request to http://localhost:8080/compile with json body {"model": "deepseek-coder-6.7b-instruct.Q5_K_M.gguf", instruction: code}
    const response = await fetch('http://localhost:8080/compile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({model: "deepseek-coder-6.7b-instruct.Q5_K_M.gguf", instruction: code})
    });
    
    // Read the resulted text from the response and store it in a variable called result
    const result = await response.text();
    
    // Search the script element with ID 'dev' and if it exists remove it
    const existingScript = document.getElementById('dev');
    if (existingScript) {
        existingScript.remove();
    }
    
    // Create a new script element with ID 'dev' and set its inner text to the result
    const newScript = document.createElement('script');
    newScript.id = 'dev';
    newScript.text = result;
    document.body.appendChild(newScript);
    
    // Return result 
    return result;
};


```