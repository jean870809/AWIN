import random
 
def diff(guess,ans):
    d=0
    for i in range(len(ans)):
        d=d+abs(ans[i]-guess[i])   
    return d

answer=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
guess=[]
for i in range(len(answer)):
    guess.append(random.randint(0,9)) 
#初始解
times=0
record=[]



for i in range(10000):
    best_d=diff(answer,guess)
    if best_d==0:
        break
    bestguess = guess
    l = list(range(len(answer)*2))
    random.shuffle(l)
    for j in range(len(l)):
        for k in range(len(answer)*2):
            if l[j] == k:
                guess[int(k/2)] = (guess[int(k/2)]+(-1)**k)%10
                now_d = diff(answer,guess)
        #times = times +1
        #record.append(now_d)
        if best_d > now_d:
            bestguess = guess
            times = times +1
            best_d = now_d
            record.append(now_d)  
            break
    
print(times)
print(len(record))
print(bestguess)

with open("hc_20.txt","w") as f:
    for r in record:
        f.write(str(r))
        f.write("\n")

