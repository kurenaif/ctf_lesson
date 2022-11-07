import random
import sys
import ctypes

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

def main(bits, original):
    assert len(original) == 5
    N = len(original)-1

    for i in range(len(original)):
        original[i] = original[i] << (48-bits)

    lcg = LCG(0)

    ys = []
    for i in range(N):
        ys.append((original[i+1] - original[i]) % (1 << 48))

    a = 0x5DEECE66D
    c = 0xB

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
    zs = Z + ys

    z = int(zs[0])

    var('x')
    cands = solve_mod((a-1)*x == (z-c), M)

    for cand in cands:
        cand = cand[0]
        lcg = LCG(0)
        lcg.set_seed(int(cand))
        check = []
        for i in range(N):
            check.append(lcg.next(bits) << (48-bits))
        if check == original[1:]:
            return lcg

bits = 16
lcg = LCG(0)
original = []

args = sys.argv
for i in range(5):
    original.append(int(args[i+1]))

lcg2 = main(bits, original)

output = []
for i in range(50):
    output.append(ctypes.c_int32(lcg2.next(32)).value)
print("next:", output)
