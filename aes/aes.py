
import state
import sbox
import gfpoly
import gfcpoly
import struct
import sys
from typing import List, Final

Nb: Final[int]  = 4

# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

def sub_bytes(st: state.State) -> state.State:
    res = []
    for c in range(4):
        for r in range(4):
            res.append(sbox.s_box(st.get(r, c)))
    return state.State(res)

def shift_rows(st: state.State) -> state.State:
    res = state.State([])

    for r in range(4):
        for c in range(4):
            res.set(r,c,st.get(r,(c + r)%4))

    return res

def mix_columns(st: state.State) -> state.State:
    res = state.State([])

    # a(x) = {03}x^3 + {01}x^2 + {01}x + {02}
    a_poly = gfcpoly.GFCPolynomial([0x02, 0x01, 0x01, 0x03])

    for c in range(4):
        s_poly = gfcpoly.GFCPolynomial([st.get(0,c), st.get(1,c), st.get(2,c), st.get(3,c)])
        sdash = (a_poly * s_poly).get_cs()

        for r in range(4):
            res.set(r,c, sdash[r].get_coeffs())

    return res

def word2byte_array(word: int) -> List[int]:
    byte_array = []

    for i in range(4):
        byte_array.append(word & 0xff)
        word >>= 8

    return byte_array

def byte_array2word(byte_array: List[int]) -> int:
    res = 0
    for b in reversed(byte_array):
        res <<= 8
        res += b
    return res

def add_round_key(st: state.State, key_schedule_words :List[int]) -> state.State:
    res = state.State([])


    for c in range(4):
        s_poly = gfcpoly.GFCPolynomial([st.get(0,c), st.get(1,c), st.get(2,c), st.get(3,c)])
        w = key_schedule_words[c]

        byte_array = word2byte_array(w)

        w_poly = gfcpoly.GFCPolynomial(byte_array)

        sdash = s_poly + w_poly

        for r in range(4):
            res.set(r,c, sdash.get_cs()[r].get_coeffs())

    return res

def sub_word(word: int) -> int:
    """ 5.3 Key Expansion SubWord() p.19. word -> [sbox(a0),sbox(a1),sbox(a2),sbox(a3)] -> sub_word

    :param word: 1 word integer
    :type word: int
    :rtype: int
    """
    byte_array = word2byte_array(word)

    return byte_array2word(list(map(lambda x:sbox.s_box(x), byte_array)))

def rot_word(word: int) -> int:
    """5.3 Key Expasion RotWord. [a0, a1, a2, a3] -> [a1, a2, a3, a0]

    :param word: 1 word integer
    :type word: int
    :rtype: int
    """
    byte_array = word2byte_array(word)
    assert(len(byte_array) == 4)

    res_byte_array = byte_array[1:] + byte_array[:1]

    res = byte_array2word(res_byte_array)

    return res


def key_expantion(key: List[int], Nk: int, Nb: int, Nr: int) -> List[int]:

    # rconの導出
    rcon = []

    rcon.append(0) # rcon[0] will not be accessed
    for i in range(1, Nb*(Nr+1)//Nk + 1):
        poly = gfpoly.GFPolynomial(1<<(i-1))
        rcon.append(byte_array2word([poly.get_coeffs(), 0, 0, 0]))

    # 鍵はbyte array
    assert(len(key) == 4*Nk)
    for b in key:
        assert(b < 256)

    w = [0] * Nb*(Nr+1)

    for i in range(Nk):
        w[i] = byte_array2word(key[4*i:4*i+4])

    for i in range(Nk, Nb*(Nr+1)):
        temp = w[i-1]
        if i % Nk == 0:
            temp = sub_word(rot_word(temp)) ^ rcon[i//Nk]
        elif Nk > 6 and i % Nk == 4:
            temp = sub_word(temp)

        w[i] = w[i-Nk] ^ temp

    return w


def cipher(input_bytes: List[int], w: List[int], Nb: int, Nr: int) -> List[int]:
    assert(len(input_bytes) == 4*Nb)

    st = state.State(input_bytes)

    st = add_round_key(st, w[0:Nb])

    for r in range(1,Nr):
        st = sub_bytes(st)
        st = shift_rows(st)
        st = mix_columns(st)
        st = add_round_key(st, w[r*Nb: (r+1)*Nb])

    st = sub_bytes(st)
    st = shift_rows(st)
    st = add_round_key(st, w[Nr*Nb:(Nr+1)*Nb])

    return st.get_bytes()

def encrypt(input_bytes: List[int], cipher_key: List[int]) -> List[int]:

    # Figure 4. Key-Block-Round Combinations
    if len(cipher_key) == 16: # AES-128
        Nk = 4
        Nr = 10
    elif len(cipher_key) == 24: # AES-192
        Nk = 6
        Nr = 12
        print("AES-192(Nk = 6) have not been not tested yet :( sorry", file=sys.stderr)
    elif len(cipher_key) == 32: # AES-256
        Nk = 8
        Nr = 14
        print("AES-256(Nk = 8) have not been not tested yet :( sorry", file=sys.stderr)
    else:
        raise ValueError("cipher_key byte length must be 16, 24, or 32")

    w = key_expantion(cipher_key, Nk, Nb, Nr)
    return bytearray(cipher(input_bytes, w, Nb, Nr))

# # Appendix B
# input_bytes = [0x32,0x43,0xf6,0xa8,0x88,0x5a,0x30,0x8d,0x31,0x31,0x98,0xa2,0xe0,0x37,0x07,0x34]
# cipher_key = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
# Nb = 4
# Nk = 4
# Nr = 10
# 
# w = key_expantion(cipher_key, Nk, Nb, Nr)
# cipher_text = cipher(input_bytes, w, Nb, Nr)
# 
# # Appendix C
# plain_text = 0x00112233445566778899aabbccddeeff
# key = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
# Nk = 8
# Nr = 14
# input_bytes = plain_text.to_bytes(16, byteorder='big')
# cipher_key = key.to_bytes(32, byteorder='big')
# w = key_expantion(cipher_key, Nk, Nb, Nr)
# cipher_text = cipher(input_bytes, w, Nb, Nr)
