## osbase_global-objects
### Instruction: 1
<pre style='text-wrap: wrap'>You are an AI programming assistant that generates only JS and CSS code.
### Instruction:
  

 Create a new empty object `os` on the window global object 
### Response:
</pre>
#### Output: 0
<pre style='text-wrap: wrap'>```javascript
if (typeof window !== 'undefined') {
    window.os = {};
} else {
    console.error("This script is meant to run in a browser environment.");
}

```</pre>
