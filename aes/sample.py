from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import aes

key = 0x000102030405060708090a0b0c0d0e0f.to_bytes(16, 'big')
plain_text = b"I am kurenaif!!!"
cipher = AES.new(key, AES.MODE_ECB)

# ciphertext = cipher.encrypt(plain_text)

cipher_text = aes.encrypt(plain_text, key)

assert(cipher.decrypt(cipher_text) == plain_text)
print("plain text:", plain_text)
print("cipher text:", cipher_text)
print("decrypt by pycryptdome: ", cipher.decrypt(cipher_text))

# plain text: b'I am kurenaif!!!'
# cipher text: bytearray(b'\xcc\xd4nc\x9cA=\x9f,K\xd7\xdeQ\x86\xff\x85')
# decrypt by pycryptdome:  b'I am kurenaif!!!'
