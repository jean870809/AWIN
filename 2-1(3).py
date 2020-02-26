import matplotlib.pyplot as plt
# import字型管理套件
from matplotlib.font_manager import FontProperties
# 指定使用字型和大小
myfont = FontProperties(fname='D:/python/NotoSansCJKtc-Black.otf', size=15)

r=500
es=[]
with open("es.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        es.append(int(line))


hc=[]
with open("hc.txt", "r") as f:
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

plt.ylim(0, 18) #y軸刻度

ES, = plt.plot(times,es[:r],color='blue')
HC, = plt.plot(times,hc[:r],color='orange')

legend = plt.legend(handles=[ES,HC,],labels = ['ES','HC'],prop=myfont,loc = 'best') #圖例

plt.title("迭代下降圖")
plt.show()