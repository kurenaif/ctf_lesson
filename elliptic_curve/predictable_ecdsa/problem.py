import random
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flag import flag

# secp256k1
bitsize = 256
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
d = random.randrange(1,n)

# ref: https://ja.wikipedia.org/wiki/%E6%A5%95%E5%86%86%E6%9B%B2%E7%B7%9A%E6%9A%97%E5%8F%B7#:~:text=%E6%A5%95%E5%86%86%E6%9B%B2%E7%B7%9A%E6%9A%97%E5%8F%B7%EF%BC%88%E3%81%A0%E3%81%88%E3%82%93,%E3%81%AE%E6%A0%B9%E6%8B%A0%E3%81%A8%E3%81%99%E3%82%8B%E6%9A%97%E5%8F%B7%E3%80%82&text=%E5%85%B7%E4%BD%93%E7%9A%84%E3%81%AA%E6%9A%97%E5%8F%B7%E6%96%B9%E5%BC%8F,%E6%96%B9%E5%BC%8F%E3%81%AE%E7%B7%8F%E7%A7%B0%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82
# calculate p1 + p2
def plus(p1, p2):
    if p1 == None:
        return p2
    if p2 == None:
        return p1

    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    phi = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    psi = ((y1*x2 - y2*x1) * pow(x2 - x1, -1, p)) % p

    x3 = (phi*phi - x1 - x2) % p
    y3 = (-phi * x3 - psi) % p
    return (x3, y3)

# calculate p1 + p1
def double(p1):
    x = p1[0]
    y = p1[1]

    phi = (((3 * x*x + a) % p) * pow(2 * y, -1, p)) % p
    psi = (((-3*x*x*x - a*x + 2*y*y) % p) * pow(2 * y, -1, p)) % p

    x4 = (phi*phi - 2 * x) % p
    y4 = (- phi * x4 - psi) % p
    return (x4, y4)

# calculate dP
def mul(d, point):
    # please implementation :)
    return None


point = (Gx, Gy)

hm = random.randrange(1, 2 ** 64)
k = random.randrange(1, n)
r = mul(k, point)[0]
s = (hm + r*d) * pow(k, -1, n) % n
print("hm = ", hm)
print("r = ", r)
print("s = ", s)
print("k = ", k)

m = hashlib.sha256()
m.update(long_to_bytes(d))
key = m.digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(flag, 16))
key = bytes_to_long(key)

print('ciphertext =', ciphertext)
