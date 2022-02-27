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
mage.physicalAttack()
mage.magicalAttack()

let mage2 = new Mage("kurenaif2", 10, 100)
mage2.physicalAttack()
mage2.magicalAttack()

let human = new Human("human", 10)
human.physicalAttack()

// ↓ mage.physicalAttack
// ↓ Mage.prototype.physicalAttack
// ↓ Human.prototype.physicalAttack
// ↓ Object.prototype.physicalAttack
