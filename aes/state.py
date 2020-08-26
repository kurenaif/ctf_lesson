from typing import List

class State:
    """3.4 The State"""

    def __init__(self, b: List[int]):
        self.s: List[int] = [0] * 16
        assert(len(b) <= 16)
        l = min(16, len(b))
        for i in range(l):
            self.s[i] = b[i]
    
    def get(self, r: int, c: int) -> int:
        """ eq (3.3)

        :param r: row 
        :type r: int
        :param c: column 
        :type c: int
        :rtype: int
        """
        return self.s[r + 4*c]

    def get_bytes(self) -> List[int]:
        return self.s

    def set(self, r: int, c: int, value: int) -> None:
        self.s[r + 4*c] = value
    
    def pprint(self) -> str:
        res = ""
        for r in range(4):
            res += "-------------\r\n"
            res += "|"
            for c in range(4):
                res += "{:02x}".format(self.get(r,c)) + "|"
            res += "\r\n"
        res += "-------------\r\n"
        return res
