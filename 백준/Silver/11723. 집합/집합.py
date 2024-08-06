import sys
input=sys.stdin.readline
M=int(input())
S=set()

for i in range(M):
    a=input().strip().split()
    if len(a)==1:
        if a[0]=='all':
            S=set([i for i in range(1, 21)])
        else:
            S=set()
        continue
    word=a[0]
    num=int(a[1])
    if word=='add':
        S.add(num)
        continue
    elif word=='remove':
        S.discard(num)
    
    elif word=='check':
        print(1 if num in S else 0)
    
    elif word=='toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)