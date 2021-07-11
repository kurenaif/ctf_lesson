def f(x0, x1, x2):
    return 338*x0 + 398*x1 + 398*x2

arr = set()
N = 100
for i in range(N):
    for j in range(N):
        for k in range(N):
            value = f(i-N//2,j-N//2,k-N//2)
            if -500 < value < 500:
                arr.add(value)


import numpy as np
import matplotlib.pyplot as plt
import pylab

#テキトーな配列を生成
rand_size = len(arr) #配列のサイズ
rand = arr
rand = sorted(list(rand)) #ソート
y = [0]*rand_size #y=0

#数直線
fig,ax=plt.subplots(figsize=(10,10)) #画像サイズ
fig.set_figheight(1) #高さ調整
ax.tick_params(labelbottom=True, bottom=False) #x軸設定
ax.tick_params(labelleft=False, left=False) #y軸設定

xmin, xmax= min(arr), max(arr)
plt.tight_layout() #グラフの自動調整
plt.scatter(rand,y,c='r') #散布図
plt.hlines(y=0,xmin=xmin,xmax=xmax) #横軸
# plt.vlines(x=[i for i in range(xmin,xmax+1,1)],ymin=-0.04,ymax=0.04) #目盛り線（大）
# plt.vlines(x=[i/10 for i in range(xmin*10,xmax*10+1,1)],ymin=-0.02,ymax=0.02) #目盛り線（小）
# line_width=(xmax-xmin)/10#目盛り数値の刻み幅
# plt.xticks(np.arange(xmin,xmax+line_width,line_width)) #目盛り数値
pylab.box(False) #枠を消す

plt.savefig("a.pdf")
