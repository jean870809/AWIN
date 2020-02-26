import matplotlib.pyplot as plt
# import字型管理套件
from matplotlib.font_manager import FontProperties
# 指定使用字型和大小
myfont = FontProperties(fname='D:/python/NotoSansCJKtc-Black.otf', size=40)

r=2000
es=[]
with open("es_20.txt", "r") as f: #讀取數據
    for line in f.readlines():
        line = line.strip('\n')
        es.append(int(line))


hc=[]
with open("hc_20.txt", "r") as f: #讀取數據
    for line in f.readlines():
        line = line.strip('\n')
        hc.append(int(line))

for i in range(r-len(hc)):
    hc.append(0)

times=[]
for i in range(r):
    times.append(i)

plt.style.use('bmh')
fig = plt.figure()
ax = plt.axes() #畫格線

plt.title("迭代下降圖", fontproperties=myfont) #標題

plt.ylim(0, 100) #y軸刻度
plt.plot(times,es[:r],color='blue')
plt.plot(times,hc[:r],color='orange')
plt.title("迭代下降圖")
plt.show()