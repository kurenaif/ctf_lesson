"use strict";

class Human {
    constructor(name, hp) {
        this.name = name
        this.hp = hp;
    }
     
    physicalAttack() {
        console.log(this.name + "'s physical Attack")
        this.hp -= 1;
    }

    // 静的関数の説明をする
    static stFunc() {
        console.log("stFunc called");
    }
}

// 継承の説明をする
class Mage extends Human {
    constructor(name, hp, mp) {
        super(name, hp);
        this.mp = mp;
    }

    magicalAttack() {
        console.log(this.name + "'s magical Attack")
        this.mp -= 1;
    }

    // このtoString()を有効にしたらtoString()はObjectのものではなくこっちが呼ばれる
    /*
    toString() {
        return "name: ", this.name;
    }
    */
}

Human.prototype.func = function(){
    console.log("kurenaif");
}

let mage = new Mage("kurenaif", 10, 100)

console.log(mage.hp)
mage.physicalAttack() // Mage から Human へ行けることの説明
mage.magicalAttack()
console.log(mage.mp)


console.log(mage.__proto__ == Mage.prototype)
console.log(mage.__proto__.magicalAttack)
console.log(mage.__proto__.magicalAttack == Mage.prototype.magicalAttack)
console.log(mage.__proto__.__proto__ == Human.prototype)
console.log(mage.__proto__.__proto__.physicalAttack)
console.log(mage.__proto__.__proto__.physicalAttack == Human.prototype.physicalAttack)
console.log(mage.__proto__.__proto__.__proto__== Object.prototype)
console.log(Mage.stFunc) // -> Function
console.log(mage.stFunc) // -> undefined 静的関数は呼ぶことができない
console.log(mage.__proto__.stFunc) // これがundefined

// Mage の toString() は Object の toString が呼ばれる
console.log(mage.toString())

// ↓ 後付も可能
console.log(mage.newFunc);
Mage.prototype.newFunc = function(){
    console.log("newFunc called;");
}
console.log(mage.newFunc());

// Objectも汚染可能 :)
mage.__proto__.__proto__.__proto__.toString = function() {
    console.log("polluted!!")
}
console.log(mage.toString())

let obj = {}
obj.toString(); // 関係ないオブジェクトもこれで汚染