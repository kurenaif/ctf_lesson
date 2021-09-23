from gfpoly import GFPolynomial
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Cipher import AES
import struct

# p.7
def ghash(H: bytes,A: bytes,C: bytes):
    lenA = len(A) * 8
    lenC = len(C) * 8
    A += b"\x00" * (16 - (len(A) % 16)) if len(A) % 16 != 0 else b""
    C += b"\x00" * (16 - (len(C) % 16)) if len(C) % 16 != 0 else b""

    As = [GFPolynomial(bytes_to_long(A[i:i + 16]), 128) for i in range(0, len(A), 16)]
    Cs = [GFPolynomial(bytes_to_long(C[i:i + 16]), 128) for i in range(0, len(C), 16)]
    H = GFPolynomial(bytes_to_long(H), 128)
    m = len(As)
    n = len(Cs)
    Xs = [GFPolynomial(0, 128)] * (m+n+2)
    for i in range(1,m+1):
        Xs[i] = (Xs[i-1] + As[i-1]) * H
    for i in range(1,n+1):
        Xs[m+i] = (Xs[m+i-1] + Cs[i-1]) * H
    res = (Xs[m+n] + (GFPolynomial(((lenA << 64) + lenC), 128))) * H
    return res.coeffs.to_bytes(16, byteorder="big")

def block_encrypt(K: bytes, msg: bytes) -> bytes:
    aes = AES.new(K, AES.MODE_ECB)
    return aes.encrypt(msg)

def incr(Y: bytes) -> bytes:
    F, I = Y[:-4], Y[-4:]
    I = ((bytes_to_long(I) + 1) % (1 << 32)).to_bytes(4, byteorder="big")

    return F + I

def bytes_xor(lhs: bytes, rhs: bytes) -> bytes:
    lhs = bytes_to_long(lhs)
    rhs = bytes_to_long(rhs)
    return long_to_bytes(lhs ^ rhs)

def encrypt(P: bytes, K: bytes, IV: bytes, A: bytes):
    H = block_encrypt(K, b'\x00'*16)

    Ps = [P[i:i + 16] for i in range(0, len(P), 16)]
    n = len(Ps)

    Ys = [0]*(n+1) # note: Y[i] means Y_{i}
    if len(IV) == 12: # if len(IV) == 96bit
        Ys[0] = IV + b"\x00\x00\x00\x01"
    else:
        Ys[0] = ghash(H, b"", IV)
    for i in range(1, n+1):
        Ys[i] = incr(Ys[i-1])
    
    Cs = [b""] * n
    for i in range(n-1):
        # C_{i} = P_{i} XOR E(K, Y_{i})
        Cs[i] = bytes_xor(Ps[i], block_encrypt(K, Ys[i+1]))
    
    u = len(Ps[n-1])
    Cs[n-1] = bytes_xor(Ps[n-1], block_encrypt(K, Ys[n])[:u])

    C = b"".join(Cs)

    T = bytes_xor(ghash(H, A, C), block_encrypt(K, Ys[0]))

    return C, T

def decrypt(C: bytes, K: bytes, IV: bytes, A: bytes):
    H = block_encrypt(K, b'\x00'*16)

    Cs = [C[i:i + 16] for i in range(0, len(C), 16)]
    n = len(Cs)

    Ys = [0]*(n+1) # note: Y[i] means Y_{i}
    if len(IV) == 12: # if len(IV) == 96bit
        Ys[0] = IV + b"\x00\x00\x00\x01"
    else:
        Ys[0] = ghash(H, b"", IV)
    for i in range(1, n+1):
        Ys[i] = incr(Ys[i-1])
    
    T = bytes_xor(ghash(H, A, C), block_encrypt(K, Ys[0]))
    
    Ps = [b""] * n
    for i in range(n-1):
        # C_{i} = P_{i} XOR E(K, Y_{i})
        Ps[i] = bytes_xor(Cs[i], block_encrypt(K, Ys[i+1]))
    
    u = len(Cs[n-1])
    Ps[n-1] = bytes_xor(Cs[n-1], block_encrypt(K, Ys[n])[:u])

    P = b"".join(Ps)

    return P, T

K = long_to_bytes(0xfeffe9928665731c6d6a8f9467308308feffe9928665731c6d6a8f9467308308)
A = long_to_bytes(0xfeedfacedeadbeeffeedfacedeadbeefabaddad2)
P = long_to_bytes(0xd9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532fcf0e2449a6b525b16aedf5aa0de657ba637b39)
IV = long_to_bytes(0x9313225df88406e555909c5aff5269aa6a7a9538534f7da1e4c303d2a318a728c3c0c95156809539fcf0e2429a6b525416aedbf5a0de6a57a637b39b)
C, T = encrypt(P, K, IV, A)
print(T)
P, T = decrypt(C, K, IV, A)
print(T)
print(hex(bytes_to_long(C)))
print(hex(bytes_to_long(P)))


##################################################

# H = 0x66e94bd4ef8a2c3b884cfa59ca342b2e
# C = 0x0388dace60b6a392f328c2b971b2fe78
# 
# print(bin(0x5e2ec746917062882c85b0685353deb7))
# 
# res = (GFPolynomial(H, 128) * GFPolynomial(C, 128))
# print(hex(res.coeffs))

##################################################

# A = long_to_bytes(0)
# H = long_to_bytes(0x66e94bd4ef8a2c3b884cfa59ca342b2e)
# C = long_to_bytes(0x0388dace60b6a392f328c2b971b2fe78)
# ghash(H,A,C)

##################################################

# A = long_to_bytes(0)
# H = long_to_bytes(0xb83b533708bf535d0aa6e52980d53b78)
# C = long_to_bytes(0x42831ec2217774244b7221b784d0d49ce3aa212f2c02a4e035c17e2329aca12e21d514b25466931c7d8f6a5aac84aa051ba30b396a0aac973d58e091473f5985)
# ghash(H,A,C)

##################################################

A = long_to_bytes(0xfeedfacedeadbeeffeedfacedeadbeefabaddad2)
H = long_to_bytes(0xb83b533708bf535d0aa6e52980d53b78)
C = long_to_bytes(0x42831ec2217774244b7221b784d0d49ce3aa212f2c02a4e035c17e2329aca12e21d514b25466931c7d8f6a5aac84aa051ba30b396a0aac973d58e091)
ghash(H,A,C)