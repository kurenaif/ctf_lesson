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
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

ansx = 0xe975abe39b5ba6701253eb4d3a7cc9af7017485e36a55ac0129b6588efabd44
ansy = None # <= ?

m = hashlib.sha256()
m.update(long_to_bytes(ansy))
key = m.digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(flag, 16))
key = bytes_to_long(key)

print('ciphertext =', ciphertext)
