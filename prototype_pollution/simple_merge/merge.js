function isObject(obj) { 
	return obj !== null && typeof obj === 'object'; 
	// ↓を有効化すると constructor.prototypeが動くようになる
	// return obj !== null && (typeof obj === 'object' || typeof obj === 'function');
}


// 確実とは言い切れないけど多分 __proto__ の除去で改善可能
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

merge({}, JSON.parse('{"__proto__":{"polluted": 1}}'))
console.log({}.polluted)

merge({}, JSON.parse('{"constructor":{"prototype":{"polluted2": 1}}}'))
console.log({}.polluted2)
