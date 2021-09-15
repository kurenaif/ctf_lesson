from typing import List

class GFPolynomial:
    # 逆にしてる
    m: int = (1 << (128 - 128)) + (1 << (128 - 7)) + (1 << (128 - 2)) + (1 << (128 - 1)) + (1 << (128 - 0))

    def __str__(self) -> str:
        res = ""
        for i in range(128):
            if (self.coeffs >> i) & 1 == 1:
                if res != "":
                    res += " + "
                res += "x^{}".format(127 - i)
        return res
    
    def get_coeffs(self) -> int:
        return self.coeffs

    def __init__(self, c: int, size: int):
        for _ in range(size - 128):
            if c & 1 == 1:
                c ^= self.m
            c >>= 1
        self.coeffs: int = c

        assert(self.coeffs < self.m)

    def __add__(self, rhs):
        return GFPolynomial(self.coeffs ^ rhs.coeffs, 128)

    def __mul__(self, rhs):
        res = 0
        for i in range(127, -1, -1):
            if (rhs.coeffs >> i) & 1 == 1:
                res ^= self.coeffs
            res <<= 1
        return GFPolynomial(res, 128*2)

if __name__ == '__main__':
    a = GFPolynomial((1<<126) + (1<<127), 128)
    b = GFPolynomial((1<<126) + (1<<127), 128)
    print(a)
    print(b)
    print((a * b))

