import numpy as np
import matplotlib.pyplot as plt
 
# 乱数を生成
xs = []
ys = []
for x in range(-20, 21):
    for m in range(-50, 50):
        y = 80 * x + 128 * m
        if -100 < y < 100:
            xs.append(x)
            ys.append(y)
 
# 散布図を描画
plt.xlim(-20,20)
plt.scatter(xs, ys)

plt.xlim(4,8)
yint = range(-20,21, 5)
plt.xticks(yint)
plt.savefig("b.pdf")
