import sys
from typing import Final
import gfpoly

def s_box(b: int) -> int:
    """ 5.1.1 SubBytes() Transformation s_box

    :param b: 1 byte integer number
    :type b: int
    """

    # 5.1.1 1. bのGF2^8の逆元を取る
    b = gfpoly.inverse(gfpoly.GFPolynomial(b)).coeffs

    bdash = [0]*8
    c: Final = 0x63

    for i in range(8):
        temp = (b >> i) & 1
        for j in range(4):
            tar = ( i + j + 4 ) % 8
            temp ^= (b >> tar) & 1

        temp ^= (c >> i) & 1
        bdash[i] = temp

    res = 0
    for i in range(7, -1, -1):
        res <<= 1
        res ^= bdash[i]

    return res
