from gfpoly import GFPolynomial
from Crypto.Util.number import long_to_bytes, bytes_to_long

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
    return res.coeffs

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