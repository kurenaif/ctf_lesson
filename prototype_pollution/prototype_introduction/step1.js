let a = {}
console.log("a.kurenaif:", a.kurenaif) // => undefined

let b = ""
b.__proto__.__proto__.kurenaif = "polluted!!"

console.log("a.kurenaif:", a.kurenaif) // => polluted!
let c = ""
console.log("c.kurenaif:", c.kurenaif) // => polluted!
