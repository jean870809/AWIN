import random
 
def diff(guess,ans):
    d=abs(ans[0]-guess[0])+abs(ans[1]-guess[1])+abs(ans[2]-guess[2])+abs(ans[3]-guess[3])
    return d

answer=[3,4,5,6]
#bestguess=[0,0,0,0] #初始解
bestguess=[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
all_time = 0
times=0
record=[]


for x in range(1000000):
    for i in range(10000):
        best_d=diff(answer,bestguess)
        record.append(diff(answer,bestguess))
        if best_d==0:
            all_time = all_time + times
            break
        guess = bestguess
        list = [0, 1, 2, 3,4,5,6,7]
        random.shuffle(list)
        for j in range(len(list)):
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
            if best_d > tmp:
                bestguess = guess
                
                break
    
#print(times)
#print(bestguess)
all_time = all_time / 1000000
print(all_time)
print(len(record))