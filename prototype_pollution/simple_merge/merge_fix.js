// https://knqyf263.hatenablog.com/entry/2020/08/09/234544

function isObject(obj) { 
	return obj !== null && typeof obj === 'object'; 
	// ↓を有効化すると constructor.prototypeが動くようになる
	// return obj !== null && (typeof obj === 'object' || typeof obj === 'function');
}


// 確実とは言い切れないけど多分 __proto__ の除去で改善可能 (functionが入るとconstructor.prototypeに対して脆弱)
function merge(a, b) {
	for (let key in b) {
		// 修正例2(不完全だけど今回は守れる)
		/*
		if(key === '__proto__') {
			continue;
		}
		*/
		if (isObject(a[key]) && isObject(b[key])) { 
			merge(a[key], b[key]); 
		} else { 
			a[key] = b[key]; 
		}
	}
	return a; 
}

// Object.freeze(Object.prototype) // 修正例1

merge({}, JSON.parse('{"__proto__":{"polluted": 1}}'))
console.log({}.polluted)

merge({}, JSON.parse('{"constructor":{"prototype":{"polluted2": 2}}}'))
console.log({}.polluted2)

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/create 何もないオブジェクトだよ
merge(Object.create(null), JSON.parse('{"__proto__":{"polluted3": 3}}'))
console.log({}.polluted3)

// でもObject.createは…
let nullObject = Object.create(null)
let normalObject = {}
nullObject.kurenaif = 12345
normalObject.kurenaif = 12345
// nullObject.toString() // ここで例外
normalObject.toString()

let a = merge({}, JSON.parse('{"a": "a"}'))
console.log(a.a)

// ロジックによってはこういうのものありだね(mass assignment対策的にやるなら)
console.log(normalObject.hasOwnProperty('kurenaif')) // => true
console.log(normalObject.hasOwnProperty('__proto__')) // => false
