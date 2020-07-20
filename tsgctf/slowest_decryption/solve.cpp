#include <fstream>
#include <bitset>
#include <vector>
#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <map>
#include <chrono>

using namespace std;

namespace mp = boost::multiprecision;
using BigInteger = mp::cpp_int;
BigInteger two_inv("34683148445144700751093233357162045663593511625090611837621255573668857186425128102741359544008411060511862885257363043164439604347003235941177207813872131779975343957346105715745679751948139701898290682990612511532874828173263826240144617504478296966964285728850389828015366614655441236440030415916175712759");

// x^n % mod
// O(log n)
template<typename T>
T Bint_pow(T x, int n) {
	T res = 1;
	while (n > 0) {
		if (n & 1) res = res * x;
		x = x * x;
		n >>= 1;
	}
	return res;
}

class Bint {
private:
public:
	BigInteger value;
	BigInteger MOD;
	Bint(BigInteger x) :MOD("69366296890289401502186466714324091327187023250181223675242511147337714372850256205482719088016822121023725770514726086328879208694006471882354415627744263559950687914692211431491359503896279403796581365981225023065749656346527652480289235008956593933928571457700779656030733229310882472880060831832351425517") {
		value = BigInteger(x);
		while (value < 0) value += MOD;
		value = x % MOD;
	}
	Bint(int x) :MOD("69366296890289401502186466714324091327187023250181223675242511147337714372850256205482719088016822121023725770514726086328879208694006471882354415627744263559950687914692211431491359503896279403796581365981225023065749656346527652480289235008956593933928571457700779656030733229310882472880060831832351425517") {
		value = BigInteger(x);
		while (value < 0) value += MOD;
		value = x % MOD;
	}

	void operator = (const Bint& rhs) {
		value = rhs.value;
	}
};

bool operator == (const Bint& lhs, const Bint& rhs) {
	return lhs.value == rhs.value;
}

Bint operator + (const Bint& lhs, const Bint& rhs) {
	return Bint((lhs.value + rhs.value) % lhs.MOD);
}

Bint operator += (Bint& lhs, const Bint& rhs) {
	lhs = lhs + rhs;
	return lhs;
}

Bint operator * (const Bint& lhs, const Bint& rhs) {
	return Bint(lhs.value * rhs.value % lhs.MOD);
}

Bint operator *= (Bint& lhs, const Bint& rhs) {
	lhs = lhs * rhs;
	return lhs;
}

Bint operator - (const Bint& lhs, const Bint& rhs) {
	return Bint((lhs.value - rhs.value + lhs.MOD) % lhs.MOD);
}

Bint operator -= (Bint& lhs, const Bint& rhs) {
	lhs = lhs - rhs;
	return lhs.value;
}

vector<int> Input() {
	fstream fin("encrypted.json");
	string input;
	getline(fin, input);
	input = input.substr(1, input.size() - 1);
	cout << input << endl;
	istringstream iss(input);
	string s;

	vector<int> nums;
	while (iss >> s) {
		s = s.substr(0, s.size() - 1);
		nums.push_back(stoi(s));
	}
	return nums;
}

template<class T>
void print(vector<T> v) {
	cout << "(";
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << (i + 1 != v.size() ? ", " : "");
	}
	cout << ")" << endl;
}

template<class T>
T gcd(T a, T b) {
	if (a < 0) a *= -1;
	if (b < 0) b *= -1;
	assert(a >= 0 && b >= 0);

	while (b != 0) {
		/* a, b = b, abs(mod(a, b)) */
		int r = a % b; /* 0 <= r < b */
		if (r > b / 2) r = b - r;
		a = b;
		b = r;
	}
	return a;
}

template<class T>
T gcd(vector<T> v) {
	assert(v.size() >= 1);
	T res = v[0];
	for (int i = 1; i < v.size(); ++i) {
		res = gcd(res, v[i]);
	}
	return res;
}

class prime {
private:
public:
	std::vector<int> primes;
	std::vector<bool> isPrime;
	prime(int num = 0) {
		if (num == 0) return;
		isPrime.resize(num + 1);
		fill(isPrime.begin(), isPrime.end(), true);
		int ma = sqrt(num) + 1;
		isPrime[0] = isPrime[1] = false;
		int cnt = 0;
		for (int i = 2; i <= ma; ++i) if (isPrime[i]) {
			for (int j = 2; i * j <= num; ++j) {
				isPrime[i * j] = false;
				cnt++;
			}
		}
		primes.reserve(cnt);
		for (int i = 0; i < isPrime.size(); ++i) if (isPrime[i]) {
			primes.push_back(i);
		}
	}

	bool IsPrime(int num) {
		if (num < isPrime.size()) return isPrime[num];
		for (auto p : primes) {
			if (num % p == 0) return false;
		}
		int ma = sqrt(num) + 1;
		for (int i = primes.back(); i <= ma; i += 2) {
			if (num % i == 0) return false;
		}
		return true;
	}

	std::map<int, int> GetFactor(int num) {
		std::map<int, int> res;
		int a = 2;
		auto it = primes.begin();
		while (num >= a * a) {
			if (num % a == 0) {
				res[a]++;
				num /= a;
			}
			else {
				++it;
				if (it == primes.end()) {
					break;
				}
				a = *it;
			}
		}
		res[num]++;
		return res;
	}
};

void enum_allcase(int index, int N, vector<int>& stack, vector<vector<int> >& res) {
	if (index == N) {
		res.push_back(stack);
		return;
	}
	for (int i = 0; i < N; ++i) {
		stack.push_back(i);
		enum_allcase(index + 1, N, stack, res);
		stack.pop_back();
	}
}

Bint brute_force(vector<int> nums) {
	vector<vector<int> > P;
	{
		vector<int> stack;
		enum_allcase(0, nums.size(), stack, P);
	}

	Bint ret = 0;
	for (auto& p : P) {
		Bint g = Bint(gcd(p));
		if (g == 0) continue;
		Bint h = 0;
		for (int i = 0; i < p.size(); ++i) {
			h += Bint(i) * Bint(nums[p[i]]);
		}
		ret += Bint(g) * h;
	}

	return ret;
}

// 1~Nまでのメビウス関数を計算する
vector<int> mebius(int N) {
	prime p(N + 1);

	vector<int> res;
	res.push_back(0);
	res.push_back(1);
	for (int i = 2; i <= N; ++i) {
		auto a = p.GetFactor(i);
		int r = 1;
		for (auto& aa : a) {
			if (aa.second >= 2) {
				r = 0;
				break;
			}
			r *= -1;
		}
		res.push_back(r);
	}

	return res;
}

Bint product_sum(const vector<int>& nums, int x) {
	const int N = (nums.size() - 1) / x + 1;
	Bint res = 0;
	Bint p = Bint_pow(Bint(N), nums.size() - 1);

	for (int i = 0; i < nums.size(); i += x) {
		res += nums[i] * p;
	}

	// すべて0のケースは除外
	res -= nums[0];

	res *= Bint(nums.size());
	res *= Bint(nums.size() - 1);
	res *= Bint(two_inv);

	return res;
}

int main(void) {
	std::chrono::system_clock::time_point  start, end; // 型は auto で可
	start = std::chrono::system_clock::now(); // 計測開始時間
	vector<int> nums = Input();
	//cout << brute_force(nums) << endl; // 705
	auto mu = mebius(nums.size());
	int N = nums.size();

	vector<Bint> psum;
	psum.push_back(0);
	for (int i = 1; i <= N; ++i) {
		psum.push_back(product_sum(nums, i));
	}

	Bint res = 0;
	for (int tar = 1; tar < N; ++tar) {
		cout << tar << endl;
		for (int i = tar; i <= N; i += tar) {
			res += tar * mu[i / tar] * psum[i];
		}
	}

	cout << res.value << endl;
	end = std::chrono::system_clock::now();  // 計測終了時間
	double elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count(); //処理に要した時間をミリ秒に変換

	cout << "time: " << elapsed << endl;

	return 0;
}
