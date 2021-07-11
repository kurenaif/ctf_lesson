import random
# DHの素数
p = next_prime(2^16)

# pのbit数
n = ceil(log(p, 2))

# MSBの漏洩してほしいbit数
k = ceil(sqrt(n)) + ceil(log(n, 2))

# 行列の必要な次元数
d = 2 * ceil(sqrt(n))

# MSB_k(alpha*t_i) == a_i
# alpha*t_i mod p - a_i < p/2^k

def generate_msb(k, x):
    mask = random.randrange(1,2^k)
    return x ^^ mask

def babai_cvp(basis, target_vector):
    gso, _ = basis.gram_schmidt()
    w = vector(QQ, target_vector)
    size = len(basis.rows())
    res = vector(QQ, size)
    for i in reversed(range(size)):
        l = QQ(w * gso[i]) / QQ(gso[i] * gso[i])
        y = l.round() * basis[i]
        res += y
        w = w - (l - l.round()) * gso[i] - y
    return res

mat = [
[1, 80],
[0, 128]
]
mat = Matrix(QQ, mat)
mat = mat.LLL()
target_vector = [0, 50]
print(babai_cvp(mat, target_vector))
