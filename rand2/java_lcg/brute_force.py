import random
# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes

multiplier = 0x5DEECE66D
addend = 0xB
mask = (1 << 48) - 1
BIT_LEN = 48

class LCG:
    multiplier = 0x5DEECE66D
    addend = 0xB
    mask = (1 << 48) - 1
    seed = 0

    def __init__(self, seed):
        self.seed = (seed ^ self.multiplier) & self.mask
    
    def set_seed(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed >> (48-bits)

def predict_seed(nums, bits):
    assert len(nums) >= 2
    
    prv = nums[0]
    nxt = nums[1]

    for masked in range(1 << (48-bits)):
        temp = (prv << (48-bits)) + masked
        if nxt == ((temp * multiplier + addend) & mask) >> (48 - bits):
            return temp

lcg = LCG(0)
nums = []

N = 10
for i in range(N):
    nums.append(lcg.next(32))

lcg_predict = LCG(0)
lcg_predict.set_seed(predict_seed(nums[:2], 32))

predicts = []
N = 10
for i in range(N):
    print(predicts.append(lcg_predict.next(32)))

print(nums[1:])
print(predicts)