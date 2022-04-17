let a = {}
console.log("a.kurenaif:", a.toString()) // => undefined

let b = ""
b.__proto__.__proto__.toString = ()=>{return "polluted!!"}

console.log("a.kurenaif:", a.toString()) // => polluted!
let c = {}
console.log("c.kurenaif:", c.toString()) // => polluted!
