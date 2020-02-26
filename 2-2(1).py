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

n=len(w) #個數

with open("capacity.txt", "r") as f:  #容量
    c = int(f.read())

import numpy as np
x = np.zeros([n+1,c+1],dtype=np.int)

for i in range(1,n+1):
    for j in range(c,0,-1):
        if (w[i-1]>j):
           x[i][j]= x[i-1][j] 
        else:
           x[i][j] = max(x[i-1][j],x[i-1][j-w[i-1]]+p[i-1]) 
        

       
print(x[n][c]) #最大值



item=[0]*n

def find_which_item(i,j,item):
    if i>=0:
        if x[i][j] == x[i-1][j]:#表示沒選這個
            item = find_which_item(i-1,j,item)
        elif j-w[i-1]>=0 and x[i,j] == x[i-1][j-w[i-1]]+p[i-1]:
            item[i-1] = 1
            item = find_which_item(i-1,j-w[i-1],item)
    return item

item = find_which_item(n,c,item)
print(item)

