import math
def diff(guess,ans):
    d=0
    for i in range(len(ans)):
        d=d+abs(ans[i]-guess[i])   
    return d

answer=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
guess=[]
record=[]


for i in range(10000):
    if i==0:
        for j in range(20):
            guess.append(0)
        record.append(diff(answer,guess)) 
    else:
        for j in range(20):
            guess[j]=int((i/(math.pow(10,len(answer)-j))%10))
        record.append(diff(answer,guess))
    if record[i]==0:
        break

print(len(record))
print(guess) 

with open("es_20.txt","w") as f:
    for r in record:
        f.write(str(r))
        f.write("\n")
