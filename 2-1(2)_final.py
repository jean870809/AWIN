import random
 
def diff(guess,ans):
    d=abs(ans[0]-guess[0])+abs(ans[1]-guess[1])+abs(ans[2]-guess[2])+abs(ans[3]-guess[3])
    return d

answer=[3,4,5,6]
guess=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)] #隨機產生初始解
times=0
record=[]



for i in range(10000):
    best_d=diff(answer,guess)
    if best_d==0: 
        break
    bestguess = guess
    list = [0, 1, 2, 3,4,5,6,7]
    random.shuffle(list)
    for j in range(len(list)): #隨機找一位+1或-1
        if list[j] == 0:
            guess[0] = (guess[0]+1)%10
            tmp = diff(answer,guess)
        elif list[j] == 1:
            guess[0] = (guess[0]-1)%10
            tmp = diff(answer,guess)
        elif list[j] == 2:
            guess[1] = (guess[1]+1)%10
            tmp = diff(answer,guess)
        elif list[j] == 3:
            guess[1] = (guess[1]-1)%10
            tmp = diff(answer,guess)
        elif list[j] == 4:
            guess[2] = (guess[2]+1)%10
            tmp = diff(answer,guess)
        elif list[j] == 5:
            guess[2] = (guess[2]-1)%10
            tmp = diff(answer,guess)
        elif list[j] == 6:
            guess[3] = (guess[3]+1)%10
            tmp = diff(answer,guess)
        elif list[j] == 7:
            guess[3] = (guess[3]-1)%10
            tmp = diff(answer,guess)
        times = times +1
        record.append(tmp)
        if best_d > tmp: #將新解取代現有解
            bestguess = guess
            best_d = tmp              
            break
    

print(times)
print(len(record))
print(bestguess)


with open("hc.txt","w") as f: #將數據寫成txt
    for r in record:
        f.write(str(r))
        f.write("\n")