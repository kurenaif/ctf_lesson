import random
from Crypto.Util.number import *

# 合計値
su = random.randrange(1,100)

# w の準備
w = [su]
N = 50

# 超増加列の作成(w[n] > w[0] + ... + w[n-1] を満たす数列) (秘密鍵)
for i in range(N-1):
    w.append(su + random.randrange(1,100))
    su += w[-1]

print(f"secret w: {w}")

# qはsuよりおおきいランダムな数 (秘密鍵)
q = 0
while q <= su:
   q = getRandomInteger(su.bit_length() + 1)
print(f"secret q: {q}")

# rはq以下で、なおかつqと互いに素な数 (秘密鍵)
r = q
while GCD(r,q) != 1:
    r = random.randrange(2,q)
print(f"secret r: {r}")

# beta[i] = r w[i] mod q が公開鍵
beta = list(map(lambda x: r * x % q, w))
print(f"public beta: {beta}")

# 平文(当然秘密)
ans = random.randrange(1,4)
print(f"secret answer: {ans}")

# 暗号化
cipher = 0
for i in range(N):
    # ibit目が1であれば
    if ((ans >> i) & 1) == 1:
        cipher += beta[i]
print(f"public cipher {cipher}")
