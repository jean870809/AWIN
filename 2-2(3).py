import random
import matplotlib.pyplot as plt
# import字型管理套件
from matplotlib.font_manager import FontProperties
# 指定使用字型和大小
myfont = FontProperties(fname='D:/python/NotoSansCJKtc-Black.otf', size=20)

w=[] #weights
with open("weights.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        w.append(int(line))

p=[] #profits
with open("profits.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        p.append(int(line))

n=len(w)

with open("capacity.txt", "r") as f:  
    c = int(f.read())

import numpy as np
x = np.zeros([n+1,c+1],dtype=np.int)


profits=[]
best_profits=0



for s in range(500):
    use=[]
    all_w=0
    all_p=0
    for i in range(n): #隨機產生初始解
        use.append(random.randint(0,1))
        if (use[i]==1):
            all_w=all_w+w[i]
            all_p=all_p+p[i]
            for j in range(c,all_w,-1):
                x[0][j]=all_p
    if all_w > c :
        continue
    for i in range(1,n+1):
        for j in range(c,0,-1):
            if use[i-1]==1:
                for j in range(c,w[i-1],-1):
                    x[i][j]=x[i-1][j]
                    temp=x[i][j]
                break
            if (w[i-1]>j): #動態規劃
                x[i][j]= x[i-1][j]
            else:
                if(x[i-1][j]>x[i-1][j-w[i-1]]+p[i-1]):
                    x[i][j]=x[i-1][j]
                else:
                    x[i][j] = x[i-1][j-w[i-1]]+p[i-1]
    profits.append(x[n][c])
    if x[n][c] > best_profits:
        best_profits=x[n][c]
    
    x = np.zeros([n+1,c+1],dtype=np.int)

#*************畫圖************
times=[]
for i in range(1,len(profits)+1):
    times.append(i)

plt.style.use('bmh')
fig = plt.figure()
ax = plt.axes() #畫格線

plt.title("爬山迭代下降圖", fontproperties=myfont) #標題

plt.xlim(1, len(profits)+1) #x軸刻度
plt.ylim(1400, 1600) #y軸刻度


plt.plot(times,profits,color='orange')
plt.show()