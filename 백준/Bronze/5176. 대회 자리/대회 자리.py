K=int(input())
for _ in range(K):
    cnt=0
    P, M = map(int, input().split())
    l=list(range(1, M+1))
    for i in range(P):
        s=int(input())
        if s in l:
            l.remove(s)
            cnt+=1
        else:
            continue
    print(P-cnt)
    