

# This file was *autogenerated* from the file a.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_0 = Integer(0)# ref: https://www.jstage.jst.go.jp/article/essfr/4/3/4_3_183/_pdf
R = PolynomialRing(GF(_sage_const_2 ), names=('x',)); (x,) = R._first_ngens(1)
# K.<a> = GF(2^8, name='x', modulus=x^8+x^4+x^3+x^2+1)
K = GF(_sage_const_2 **_sage_const_4 , modulus=x**_sage_const_4 +x+_sage_const_1 , impl='pari', names=('alpha',)); (alpha,) = K._first_ngens(1)
power_map = {}

for i in range(_sage_const_2 **_sage_const_4 ):
    power_map[alpha**i] = i


k = _sage_const_4 
t = _sage_const_3 
n = k+_sage_const_2 *t

I = x**_sage_const_3 +x**_sage_const_2 +x+alpha

G = _sage_const_1 
for i in range(_sage_const_1 , _sage_const_2 *t+_sage_const_1 ):
    G *= (x-(alpha**i))
P = (x**(n-k) * I) % G
C = (x**(n-k) * I) + P

y = C + (_sage_const_1  + x + x**_sage_const_5 )
# y = x + x^4 + x^6
print(y)

S = _sage_const_0 
for i in range(_sage_const_1 ,_sage_const_2 *t+_sage_const_1 ):
    S += x**(i-_sage_const_1 )*y(alpha**i)

def my_gcd(t, lhs, rhs, aprev=_sage_const_1 , aprevprev=_sage_const_0 ):
    if rhs.degree() < t:
        return rhs, aprev
    a = -(lhs//rhs) * aprev + aprevprev
    return my_gcd(t, rhs, lhs%rhs, a, aprev)

r, a = my_gcd(t, x**(_sage_const_2 *t), S)
print(r)
print(a)

gamma = _sage_const_1 /(alpha**power_map[a[_sage_const_0 ]])
# gamma = 1
sigma = gamma*a 
eta = gamma * r

error_pos = []
for i in range(_sage_const_1 , _sage_const_2 **_sage_const_4 ):
    if sigma(alpha**i) == _sage_const_0 :
        error_pos.append(_sage_const_2 **_sage_const_4 -i-_sage_const_1 )

print(error_pos)

sigma_dash = _sage_const_0 
for l in error_pos:
    temp = alpha**l
    for i in error_pos:
        if i == l:
            continue
        temp *= (_sage_const_1 -(alpha**i)*x)
    sigma_dash += temp
sigma_dash = -sigma_dash

e = _sage_const_0 
for i in error_pos:
    e += (x**i) * (-eta(alpha**(-i)) / sigma_dash(alpha**(-i)))

y -= e

print(y)
print(y//x**(n-k))

