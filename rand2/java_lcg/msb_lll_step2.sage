import random
# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes

class LCG:
    multiplier = 0x5DEECE66D
    addend = 0xB
    mask = (1 << 48) - 1
    seed = 0

    def __init__(self, seed):
        self.seed = (seed ^^ self.multiplier) & self.mask
    
    def set_seed(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed >> (48-bits)

N = 4
lcg = LCG(0)
ans = []
original = []
bits = 16
for i in range(N+1):
    ans.append(lcg.next(48))
    original.append(((ans[-1]) >> (48-bits)) << (48-bits))

ys = []
for i in range(N):
    ys.append((original[i+1] - original[i]) % (1 << 48))

a = 0x5DEECE66D
c = 0xB
print(ys[1], (ys[0] * a) % (1 << 48))

M = (1 << 48)

ys = vector(ZZ, ys)
mat = -matrix.identity(N)

for i in range(N):
    row = list(mat[i])
    if i == 0:
        row[0] = M
    else:
        row[0] = (a ** (i))
    mat[i] = vector(ZZ, row)


mat = mat.LLL()

W1 = mat * ys
W2 = vector([ round(RR(w) / M) * M - w for w in W1 ])

Z = mat.solve_right(W2)
print(Z + ys)
print(ans[1] - ans[0])

z = ans[1] - ans[0]

print((a*ans[0] + c - ans[0]) % M == z)
print(((a-1)*ans[0] + c) % M == z)
print(((a-1)*ans[0] ) % M == (z - c) % M)

var('x')
print(solve_mod((a-1)*x == (z-c), M))
print(ans[0])