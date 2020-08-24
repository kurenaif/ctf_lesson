import copy
import time
import gfpoly
from typing import List

class GFCPolynomial:
    """p.12~ 4.3 Polynomials with Coefficients in GF(2^8) """

    def pprint(self) -> str:
        res = ""
        for i in range(3,-1,-1):
            if i != 3:
                res += " + "
            res += "{{{:02x}}}*x^{}".format(self.cs[i].get_coeffs(), i)
        return res
    
    # cs[0] + cs[1] x + cs[2] x^2 + cs[3] x^3
    def __init__(self, cs: List[int]):
        assert(len(cs) <= 4)
        for c in cs:
            assert(c < 256)

        self.cs = [gfpoly.GFPolynomial(0)] * 4
        for i in range(min(4, len(cs))):
            self.cs[i] = gfpoly.GFPolynomial(cs[i])

    def __add__(self, rhs):
        res = GFCPolynomial([])
        for i in range(4): # GF(2^8) の足し算を行う
            res.cs[i] = self.cs[i] + rhs.cs[i]
        return res

    def __mul__(self, rhs):
        res = GFCPolynomial([])

        for i in range(4):
            for j in range(4):
                res.cs[(i+j)%4] = res.cs[(i+j)%4] + (self.cs[i] * rhs.cs[j])

        return res

