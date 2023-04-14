from secrets import FLAG
from Crypto.Util.number import *

FLAG = bytes_to_long(FLAG)
e = 65537
p = getPrime(512)
q = getPrime(512)
N = p * q
a = getRandomInteger(1024)

c1 = pow(FLAG, e, N)
c2 = pow(FLAG+a, e, N)
print(f"{c1=}")
print(f"{c2=}")
print(f"{N=}")
print(f"{e=}")
print(f"{a=}")