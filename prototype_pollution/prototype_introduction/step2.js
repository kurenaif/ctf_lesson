let a = {}
console.log("a.toString():", a.toString()) // => [object Object]

let b = ""
b.__proto__.__proto__.toString = ()=>{return "polluted!!"}

console.log("a.toString():", a.toString()) // => polluted!
let c = {}
console.log("c.toString():", c.toString()) // => polluted!
