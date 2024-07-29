T=int(input())

for i in range(T):
    l=list(input())
    cnt=0
    for j in l:
        if j=='U': cnt+=1
        elif j=='D':
            break
    print(cnt)

