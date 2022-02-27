// https://knqyf263.hatenablog.com/entry/2020/08/09/234544

function isObject(obj) { 
	return obj !== null && typeof obj === 'object'; 
	// ↓を有効化すると constructor.prototypeが動くようになる
	// return obj !== null && (typeof obj === 'object' || typeof obj === 'function');
}


function merge(a, b) {
	for (let key in b) {
		if (isObject(a[key]) && isObject(b[key])) { 
			merge(a[key], b[key]); 
		} else { 
			a[key] = b[key]; 
		}
	}
	return a; 
}

merge({c: 2}, JSON.parse('{"__proto__":{"polluted": 1}}'))
// let obj = merge({lkey: 2}, JSON.parse('{"rkey":{"rkeyrkey": 1}}'))

console.log({}.polluted)
a = ""
console.log(a.polluted)
