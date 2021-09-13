P.<a> = PolynomialRing(GF(2))
f = a^0 + a^1 + a^2 + a^7 + a^128
k.<x> = GF(2^128, modulus=f)
print(x^129 + 1)
