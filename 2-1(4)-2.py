import random

def diff(guess,ans):
    d=0
    for i in range(len(ans)):
        d=d+abs(ans[i]-guess[i])   
    return d

answer=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
bestguess=[]
for i in range(20):
    bestguess.append(0) 
#初始解
record=[]
record.append(diff(answer,bestguess))
times=0

for j in range(10000):
    best_d=diff(answer,bestguess)
    current_best_d=best_d
    guess=[bestguess]
    for i in range(len(answer)):
        if bestguess[i]>0:
            gue=[]
            gue.extend(bestguess[0:i])
            gue.append(bestguess[i]-1)
            gue.extend(bestguess[i+1:])
            guess.append(gue)

        if bestguess[i]<9:    
            gue=[]
            gue.extend(bestguess[0:i])
            gue.append(bestguess[i]+1)
            gue.extend(bestguess[i+1:])
            guess.append(gue)

        times+=1

        for g in guess:
            d=diff(g,answer)
            if d<best_d:
                best_d=d
                bestguess=g
                record.append(diff(answer,g)) 
    if current_best_d==0:
        break
       
print(times)
print(bestguess)

with open("hc_20.txt","w") as f:
    for r in record:
        f.write(str(r))
        f.write("\n")
        