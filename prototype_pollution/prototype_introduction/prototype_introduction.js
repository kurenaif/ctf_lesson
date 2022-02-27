class Human {
    constructor(name, hp) {
        this.name = name
        this.hp = hp;
    }
     
    physicalAttack() {
        console.log(this.name + "'s physical Attack")
        this.hp -= 1;
    }

	// toString() {
	// 	console.log(this.name + "'s hp is " + this.hp)
	// }
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

let mage = new Mage("kurenaif", 10, 100)
let mage2 = new Mage("kurenaif2", 10, 100)
let human = new Human("human", 10)
mage.toString()
// Object.prototype.toString = () => {
// 	console.log("polluted")
// }
// mage.toString();
