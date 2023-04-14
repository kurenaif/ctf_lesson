# ref: https://www.jstage.jst.go.jp/article/essfr/4/3/4_3_183/_pdf
R.<x> = PolynomialRing(GF(2))
# K.<a> = GF(2^8, name='x', modulus=x^8+x^4+x^3+x^2+1)
K.<alpha> = GF(2^4, modulus=x^4+x+1, impl='pari')
power_map = {}

for i in range(2^4):
    power_map[alpha^i] = i


k = 4
t = 3
n = k+2*t

I = x^3+x^2+x+1

G = 1
for i in range(1, 2*t+1):
    G *= (x-(alpha^i))
P = (x^(n-k) * I) % G
C = (x^(n-k) * I) + P

y = C + (1 + x + x^5)
# y = x + x^4 + x^6
print(y)

S = 0
for i in range(1,2*t+1):
    S += x^(i-1)*y(alpha^i)

def my_gcd(t, lhs, rhs, aprev=1, aprevprev=0):
    if rhs.degree() < t:
        return rhs, aprev
    a = -(lhs//rhs) * aprev + aprevprev
    return my_gcd(t, rhs, lhs%rhs, a, aprev)

r, a = my_gcd(t, x^(2*t), S)
print(r)
print(a)

gamma = 1/(alpha^power_map[a[0]])
# gamma = 1
sigma = gamma*a 
eta = gamma * r

error_pos = []
for i in range(1, 2^4):
    if sigma(alpha^i) == 0:
        error_pos.append(2^4-i-1)

print(error_pos)

sigma_dash = 0
for l in error_pos:
    temp = alpha^l
    for i in error_pos:
        if i == l:
            continue
        temp *= (1-(alpha^i)*x)
    sigma_dash += temp
sigma_dash = -sigma_dash

e = 0
for i in error_pos:
    e += (x^i) * (-eta(alpha^(-i)) / sigma_dash(alpha^(-i)))

y -= e

print(y)
print(y//x^(n-k))