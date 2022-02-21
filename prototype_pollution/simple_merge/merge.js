function isObject(obj) { 
	return obj !== null && typeof obj === 'object';
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

// 似たケース: jQueryのextend
