import random
import sys
import ctypes

# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes
# usage: sage msb_lll_step3.sage 0 11 4 7 12 3 3 8 4 7 8 0 9 2 9 7 2 8 5 8

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

def main(bits, y):
    N = len(y)-1

    for i in range(len(y)):
        y[i] = y[i] << (48-bits)

    ydashes = []
    for i in range(N):
        ydashes.append((y[i+1] - y[i]) % (1 << 48))

    a = 0x5DEECE66D
    c = 0xB
    M = (1 << 48)

    ydashes = vector(ZZ, ydashes)
    A = -matrix.identity(N)

    for i in range(N):
        row = list(A[i])
        if i == 0:
            row[0] = M
        else:
            row[0] = (a ** (i))
        A[i] = vector(ZZ, row)


    A = A.LLL()

    k = vector(ZZ, [round(RR(w) / M) for w in (A * ydashes)])
    W2 = k * M - A*ydashes

    edash = A.solve_right(W2)
    xdashes = edash + ydashes

    var('x')
    cands = solve_mod((a-1)*x == (int(xdashes[0])-c), M)

    for cand in cands:
        cand = cand[0]
        lcg = LCG(0)
        lcg.set_seed(int(cand))
        check = []
        for i in range(N):
            check.append(lcg.next(bits) << (48-bits))
        if check == y[1:]:
            return lcg

bits = 4 # top 4 bits

args = sys.argv
if len(args) < 21:
    print(f"usage: {args[0]} rand0 rand1 rand2 ... rand19")
    print(f"example: {args[0]} 1 13 1 14 5 13 3 12 12 8 1 2 7 0 6 15 14 11 14 6")
    sys.exit(1)

y = []
for i in range(20):
    y.append(int(args[i+1]))

lcg = main(bits, y)
output = []
for i in range(50):
    output.append(ctypes.c_int32(lcg.next(32)).value)
print("next:", output)
