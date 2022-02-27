class Human {
    constructor(name, hp) {
        this.name = name
        this.hp = hp;
    }
     
    physicalAttack() {
        console.log(this.name + "'s physical Attack")
        this.hp -= 1;
    }
}

class Mage extends Human {
    constructor(name, hp, mp) {
        super(name, hp);
        this.mp = mp;
    }

    magicalAttack() {
        console.log(this.name + "'s magical Attack")
        this.mp -= 1;
    }
}

// Mage.prototype.magicalAttack = () => {
// 	console.log("new MagicalAttack")
// }

// Human.prototype.physicalAttack = () => {
// 	console.log("new PhysicalAttack")
// }

let mage = new Mage("kurenaif", 10, 100)
mage.__proto__.__proto__.__proto__.physicalAttack = () => {
	console.log("new physicalAttack")
}

mage.physicalAttack()
mage.magicalAttack()

let mage2 = new Mage("kurenaif2", 10, 100)
mage2.physicalAttack()
mage2.magicalAttack()

let human = new Human("human", 10)
human.physicalAttack()

let hoge = {}
hoge.physicalAttack()

// ↓ mage
// ↓ __proto__ 
// ↓ Mage.prototype
// ↓ __proto__ 
// ↓ Human.prototype
// ↓ __proto__ 
// ↓ Object.prototype
