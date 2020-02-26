import random

def diff(guess,ans):
    d=abs(ans[0]-guess[0])+abs(ans[1]-guess[1])+abs(ans[2]-guess[2])+abs(ans[3]-guess[3])
    return d

answer=[3,4,5,6]
bestguess=[0,0,0,0] #初始解
record=[]
record.append(diff(answer,bestguess))
times=0

for j in range(10000):
    best_d=diff(answer,bestguess)
    current_best_d=best_d
    guess=bestguess
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
            
        print(guess)    
        times+=1

        d=diff(guess,answer)
        if d<best_d:
            best_d=d
            bestguess=guess
            record.append(diff(answer,guess)) 
    if current_best_d==0:
        break
       

print(times)
print(bestguess)

with open("hc.txt","w") as f:
    for r in record:
        f.write(str(r))
        f.write("\n")
        