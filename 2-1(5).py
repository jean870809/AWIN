import random
import math
import matplotlib.pyplot as plt
# import字型管理套件
from matplotlib.font_manager import FontProperties
# 指定使用字型和大小
myfont = FontProperties(fname='D:/python/NotoSansCJKtc-Black.otf', size=20)


global time,balance    #  time 迭代次數, balance  平衡次数
global T,af   # T 温度  af 退火率 
global guess,answer,best_d #best_d 目前最好的差
T=1000.0
af =0.8
time =10000  
balance = 20
bestguess=[]
nowguess=[]  #  best_guess 目前最好的猜測   now_guess 目前的猜測
record=[]  #記錄每次的差
answer=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
#answer = [3,4,5,6]
def calc(guess):  #計算與正解差的絕對值
    global answer
    d=0
    for i in range(len(answer)):
        d=d+abs(answer[i] - guess[i])   
    return d
def produce():  #產生隨機初始解
    global nowguess,best_d
    for i in range(len(answer)):
        nowguess.append(random.randint(0,9))
    best_d = calc(nowguess)
    print(nowguess,best_d)
 
def init():   #初始化函數
    global T
    produce()   
     
def slove():  #迭代函数
    global T,balance,best_d,bestguess,nowguess
    guess=nowguess
    now_d = 0   #目前的差
    for i in range(balance):
        now_d = calc(nowguess)
        best_d = now_d
        l = list(range(len(answer)*2))
        random.shuffle(l)
        for j in range(len(l)):
            for k in range(len(answer)*2):
                if l[j] == k:
                    guess[int(k/2)] = (guess[int(k/2)]+(-1)**k)%10
                    temp = calc(guess)
            if(temp < best_d): 
                best_d = temp
                bestguess = guess     #更新目前最好的解
            if(temp < now_d):
                now_d = temp       #直接接受新解
                nowguess = guess
                record.append(now_d)
                break
            else:
                g = 1.0*(now_d-temp)/T
                if(random.random() < math.exp(g)):   #概率接受劣解
                    now_d = temp 
                    nowguess = guess
                    record.append(now_d)   
                
#*****************************主函数**********************        
init()
for i in range(time):      
    slove()
    record.append(best_d)
    T = T*af    #溫度下降
    if best_d==0:
        print(bestguess,best_d,i)
        break


        
  

#**************************圖*************
times=[]
for i in range(1,len(record)+1):
    times.append(i)

plt.style.use('bmh')
fig = plt.figure()
ax = plt.axes() #畫格線

plt.title("退火迭代下降圖", fontproperties=myfont) #標題

plt.xlim(1, len(record)+1) #x軸刻度
plt.ylim(0,100) #y軸刻度


plt.plot(times,record,color='orange')
plt.show()

