import copy
import time
from typing import List

class GFPolynomial:
    """p.10~ 4. Mathemaical Preliminaries(4.1, 4.2)"""

    # modulo x^8 + x^4 + x^3 + x + 1
    m: int = 0x11b

    def pprint(self) -> str:
        res = ""
        for i in range(7, -1, -1):
            if (self.coeffs >> i) & 1 == 1:
                if res != "":
                    res += " + "
                res += "x^{}".format(i)
        return res
    
    def get_coeffs(self) -> int:
        return self.coeffs

    def __init__(self, c: int):
        if c >= 0x100:
            temp_m = self.m << (c.bit_length() - self.m.bit_length())
            
            tar = c.bit_length()

            while(c >= 0x100):
                if (c >> (tar - 1)) & 1 == 1:
                    c ^= temp_m
                temp_m >>= 1
                tar -= 1

        self.coeffs: int = c
        assert(self.coeffs < self.m)

    def __add__(self, rhs):
        return GFPolynomial(self.coeffs ^ rhs.coeffs)

    def __mul__(self, rhs):
        res = 0
        for i in range(8):
            for j in range(8):
                if ((self.coeffs >> i) & 1) == 1 and ((rhs.coeffs >> j) & 1) == 1:
                    res ^= (1 << (i+j))
        return GFPolynomial(res)

# 乗法的逆元の計算
__inverse: List[GFPolynomial] = [GFPolynomial(0)] * 256
for i in range(256):
    for j in range(256):
        res = GFPolynomial(i) * GFPolynomial(j)
        if res.coeffs == 1:
            __inverse[i] = GFPolynomial(j)

def inverse(poly: GFPolynomial) -> GFPolynomial:
    return __inverse[poly.coeffs]
