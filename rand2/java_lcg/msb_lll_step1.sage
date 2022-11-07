import random
# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes

class LCG:
    multiplier = 0x5DEECE66D
    # addend = 0xB
    addend = 0
    mask = (1 << 48) - 1
    seed = 0

    def __init__(self):
        self.seed = random.randint(0, self.mask)

    def next(self):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed

lcg = LCG()

anses = []
ys = []

N = 4
MASK_SIZE = 48
HIDE_SIZE = 32
for i in range(N):
    temp = lcg.next()
    anses.append(temp)
    ys.append(temp & ((1<<(MASK_SIZE-HIDE_SIZE))-1 << HIDE_SIZE))

print(anses)

a = 0x5DEECE66D
M = (1 << 48)

ans = vector(ZZ, anses)
ys = vector(ZZ, ys)
mat = -matrix.identity(N)

for i in range(N):
    row = list(mat[i])
    if i == 0:
        row[0] = M
    else:
        row[0] = int((a ** (i)) % M)
    mat[i] = vector(ZZ, row)


print(mat)
res = mat * ans
print(res)

original_mat = mat
mat = mat.LLL()
res = mat * ans 

W1 = mat * ys
W2 = vector([ round(RR(w) / M) * M - w for w in W1 ])

Z = mat.solve_right(W2)
print("--------------------------------------------------")
print(Z + ys)
print(ans)

print("--------------------------------------------------")
print(mat*Z)
temp = original_mat*Z
print(f"Ae={temp[0]}")
print(f"Ae={temp[1]}")
print(f"Ae={temp[2]}")
print(f"Ae={temp[3]}")
print(f" M={M}")