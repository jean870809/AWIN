import random

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
temp = -1
all_w=0
all_p=0
#use = np.zeros(15,dtype=np.int)


use = [1,0,0,0,1,0,0,0,0,1,1,0,0,0,1]
for i in range(n): #隨機產生初始解
    #use.append(random.randint(0,1))
    if (use[i]==1):
        all_w=all_w+w[i]
        all_p=all_p+p[i]
        for j in range(c,all_w,-1):
           x[0][j]=all_p
  
for i in range(1,n+1):
    for j in range(c,0,-1):
        if use[i-1]==1:
            for j in range(c,w[i-1],-1):
                x[i][j]=x[i-1][j]
                temp=x[i][j]
            break
        if (w[i-1]>j): #動態規劃
            x[i][j]= x[i-1][j]
            #temp=x[i][j] 
        else:
            if(x[i-1][j]>x[i-1][j-w[i-1]]+p[i-1]):
                x[i][j]=x[i-1][j]
                #temp=x[i][j]
            else:
                use[i]=1
                x[i][j] = x[i-1][j-w[i-1]]+p[i-1]
                #temp=x[i][j]




#print(use)
print(x[n][c])
#print(profits)        
#print(best_profits)      
max=np.argwhere(x==best_profits)

with open("test.txt","w") as f:
    for r in x:
        f.write(str(r))
        f.write("\n")

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
