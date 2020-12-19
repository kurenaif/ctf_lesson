from ptrlib import *
import base64
import sys
from typing import List
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import copy
import time

def bytearray_to_blocks(barray: bytearray) -> List[int]:
    if len(barray) % 16 != 0:
        print("len(barray) % 16 must be 0", file=sys.stderr)

    blocks = [[]]

    for i in range(len(barray)):
        if len(blocks[-1]) == 16 :
            blocks.append([])
        blocks[-1].append(barray[i])
    
    return blocks

def blocks_to_bytearray(barray: List[List[int]]) -> bytearray:
    res = bytearray()
    for i in range(len(barray)):
        for j in range(len(barray[i])):
            res.append(barray[i][j])
    return res

sock = Socket("localhost", 2000)
sock.recvuntil("flag is here!: ")
cipher_text = base64.b64decode(sock.recvline())
cipher_blocks_org = bytearray_to_blocks(cipher_text)

res = []
while len(cipher_blocks_org) > 1:
    cipher_blocks = copy.deepcopy(cipher_blocks_org)
    temp_res = [0] * 16
    for j in range(16):
        block = [0] * 16
        for i in range(256):
            time.sleep(0.01)
            if j == 0 and cipher_blocks[-2][-1-j] == i:
                continue

            sock.recvuntil("cipher_text: ")

            temp_blocks = copy.deepcopy(cipher_blocks)
            temp_blocks[-2][-1-j] = i

            sock.sendline(base64.b64encode(blocks_to_bytearray(temp_blocks)))

            sock.recvuntil("result: ")
            result = 'ok' in sock.recvline().decode('utf-8')

            if result:
                index = 16-j-1
                ans = (j+1) ^ cipher_blocks[-2][-1-j] ^ i
                cipher_blocks[-2][-1-j] = i ^ (j+1) ^ (j+2)
                temp_res[index] = ans
                for k in range(j):
                    cipher_blocks[-2][-1-k] ^= (j+1) ^ (j+2)
                print(bytearray(temp_res))
                time.sleep(1)
                break

    res = temp_res + res
    cipher_blocks_org = cipher_blocks_org[:-1]

print(bytearray(res))
