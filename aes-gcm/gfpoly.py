from typing import List

class GFPolynomial:
    m: int = (1 << 128) + (1 << 7) + (1 << 2) + (1 << 1) + 1

    def pretty(self) -> str:
        res = ""
        for i in range(128, -1, -1):
            if (self.coeffs >> i) & 1 == 1:
                if res != "":
                    res += " + "
                res += "x^{}".format(i)
        return res
    
    def get_coeffs(self) -> int:
        return self.coeffs

    def __init__(self, c: int):
        if c >= (1 << 128):
            temp_m = self.m << (c.bit_length() - self.m.bit_length())
            
            tar = c.bit_length()

            while(c >= (1 << 128)):
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
        for i in range(128):
            for j in range(128):
                if ((self.coeffs >> i) & 1) == 1 and ((rhs.coeffs >> j) & 1) == 1:
                    res ^= (1 << (i+j))
        return GFPolynomial(res)

if __name__ == '__main__':
    print(GFPolynomial((1<<129) + 1).pretty())
