import sys
from typing import List
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = b"00000000000000000000000000000000"

def bytearray_to_blocks(barray: bytearray) -> List[int]:
    blocks = [[]]

    for i in range(len(barray)):
        if len(blocks[-1]) == 16 :
            blocks.append([])
        blocks[-1].append(barray[i])
    
    return blocks

def print_bytearray(barray: bytearray):
    blocks = bytearray_to_blocks(barray)
    for i in range(len(blocks)):
        block = blocks[i]
        print(f"block {i}: ", end="", file=sys.stderr)
        for num in block:
            print(f"|{num:02x}", end="", file=sys.stderr)
        print("|", file=sys.stderr)

def pad(barray: bytearray) -> bytearray:
    pad_length = 16 - (len(barray) % 16)
    for _ in range(pad_length):
        barray.append(pad_length)
    return barray

def unpad(barray: bytearray) -> bytearray:
    if barray[-1] == 0 or barray[-1] > 16:
        raise Exception("padding error")
    if len(barray) == 0 or len(barray) % 16 != 0:
        raise Exception("padding error")

    pad_length = barray[-1]

    for i in range(pad_length):
        if barray[-i-1] != pad_length:
            raise Exception("padding error")

    return barray[:-pad_length]

def encrypt(plain_text: bytearray):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(plain_text)
    print("encrypted text:", file=sys.stderr)
    print_bytearray(cipher_text)
    print(file=sys.stderr)

    return iv + cipher_text

def decrypt(cipher_text: bytearray):
    iv = cipher_text[:16]
    cipher_text = cipher_text[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text)
    print("decrypted text (debug):", file=sys.stderr)
    print_bytearray(plain_text)
    print(file=sys.stderr)
    return plain_text

plain_text = bytearray(b"kurenaifCTF{hogehogehogehoge_fugafugafugafuga}")
print("plain_text: ")
print_bytearray(plain_text)

cipher_text = bytearray(encrypt(pad(plain_text)))

print("flag is here!:", base64.b64encode(cipher_text).decode('utf-8'), end="\n\n")

while(True):
    cipher_text = base64.b64decode(input("cipher_text: "))
    plain_text = decrypt(cipher_text)
    try:
        unpad(plain_text)
        print("result: ok!")
        print("result: ok!", file=sys.stderr)
    except:
        print("result: padding error")
        print("result: padding error", file=sys.stderr)
    print("----------------------------", file=sys.stderr)
