def diff(guess,ans): #計算與正解相差的絕對值
    d=abs(ans[0]-guess[0])+abs(ans[1]-guess[1])+abs(ans[2]-guess[2])+abs(ans[3]-guess[3])
    return d

answer=[3,4,5,6]
guess=[] #猜測密碼
record=[] #將每次的差紀錄起來


for i in range(10000):
    if i==0: 
        guess.append(0)
        guess.append(0)
        guess.append(0)
        guess.append(0)
        record.append(diff(answer,guess)) 
    else:
        guess[0]=int((i/1000)%10)
        guess[1]=int((i/100)%10)
        guess[2]=int((i/10)%10)
        guess[3]=int(i%10)
        record.append(diff(answer,guess))
    if record[i]==0:
        break

print(len(record))
print(guess) 

with open("es.txt","w") as f: #將數據寫成txt
    for r in record:
        f.write(str(r))
        f.write("\n")
