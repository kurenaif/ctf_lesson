from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

import binascii


key = b"1234567890123456" 
data = b"hogehoge" # 暗号化する文字
target = b"fugafuga"

# 暗号化処理
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(ciphertext)

print(tag)
print(cipher.nonce)

# 復号処理
cipher_dec = AES.new(key, AES.MODE_GCM, cipher.nonce)
# dec_data = cipher_dec.decrypt_and_verify(ciphertext, tag)
dec_data = cipher_dec.decrypt(strxor(strxor(data, target), ciphertext))

print(dec_data)
