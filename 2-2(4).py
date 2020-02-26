import random
import math
import matplotlib.pyplot as plt
# import字型管理套件
from matplotlib.font_manager import FontProperties
# 指定使用字型和大小
myfont = FontProperties(fname='D:/python/NotoSansCJKtc-Black.otf', size=20)

global m,C    # m個物品 ,背包容量C
global time,balance    #  time 迭代次数, balance  平衡次数
global best,T,af   #best 紀錄全域最佳值  T 温度  af退火率
m=15
T=1000.0
af =0.95
time =500  
balance = 20 
best_way=[0]*m
now_way=[0]*m  #  best_way 全域最佳的放法   now_way 目前的放法  
weight=[]
value=[]
profits=[]
with open("weights.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        weight.append(int(line))
with open("profits.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        value.append(int(line))

def cop(a,b,le):     #將b複製到a
    for i in range(le):
        a[i]=b[i]
def calc(x):  #計算背包價值
    global C,wsum
    vsum=0
    wsum=0
    for i in range(m):
        vsum +=x[i]*value[i]
        wsum += x[i]*weight[i]    
    return  vsum
def produce():  #初始產生隨機解
    while (1>0):
        for k in range(m):
            if(random.random() < 0.5):
                now_way[k]=1
            else:
                now_way[k]=0
        calc(now_way)
        if(wsum <C):
            break
    global best
    best=calc(now_way)
    cop(best_way,now_way,m)
 
def init():   #初始化
    global C,best,T
    C = 750
    best=-1
    produce()    
def get(x):      #隨機取出背包內的物品
    while(1>0):
        ob = random.randint(0,m-1)
        if(x[ob]==1): 
            x[ob]=0
            break
def put(x):      #隨機將物品放入背包內
    while(1>0):
        ob = random.randint(0,m-1)
        if(x[ob]==0): 
            x[ob]=1
            break       
def slove():  #迭代函数
    global best,T,balance
    test=[0]*m
    now = 0   #目前背包價值
    for i in range(balance):
        now = calc(now_way)
        cop(test,now_way,m)
        ob = random.randint(0,m-1) #隨機選某個物品
        if(test[ob]==1):
            put(test)
            test[ob]=0  #在背包內就拿出來，然後放其他物品
        else:   #不在裡面就直接放或替換目前在背包內的物品
            if(random.random()<0.5):
                test[ob]=1 
            else: 
                get(test)
                test[ob]=1
        temp= calc(test)
        if(wsum>C):
            continue    # 非法解跳過
        if(temp > best): 
            best=temp
            cop(best_way,test,m)     #更新全域最佳
        
        if(temp > now):
            cop(now_way,test,m)       #直接接受新解 
        else:
            g = 1.0*(temp-now)/T
            if(random.random() < math.exp(g)):   #概率接受劣解
                cop(now_way,test,m)    
                
#*****************************主函数**********************        
init()
#isGood = 0
for i in range(time):      
    slove()
    profits.append(best)
    T = T*af    #溫度下降

        
  
print(best)
print(best_way)

#**************************圖*************
times=[]
for i in range(1,len(profits)+1):
    times.append(i)

plt.style.use('bmh')
fig = plt.figure()
ax = plt.axes() #畫格線

plt.title("退火迭代下降圖", fontproperties=myfont) #標題

plt.xlim(1, len(profits)+1) #x軸刻度
plt.ylim(1300, 1600) #y軸刻度


plt.plot(times,profits,color='orange')
plt.show()
