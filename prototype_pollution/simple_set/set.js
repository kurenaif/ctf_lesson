// https://knqyf263.hatenablog.com/entry/2020/08/09/234544

function isObject(obj) { 
	return obj !== null && typeof obj === 'object'; 
	// ↓を有効化すると constructor.prototypeが動くようになる
	// return obj !== null && (typeof obj === 'object' || typeof obj === 'function');
}

function setValue(obj, key, value) {
  const keylist = key.split('.');
  const e = keylist.shift();
  if (keylist.length > 0) {
    if (!isObject(obj[e])) obj[e] = {};

    setValue(obj[e], keylist.join('.'), value);
  } else {
    obj[key] = value;
    return obj;
  }
}

setValue({}, "__proto__.polluted", 1);
console.log({}.polluted)
setValue({}, "constructor.prototype.polluted2", 2);
console.log({}.polluted2)
