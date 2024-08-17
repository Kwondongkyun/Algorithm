N=int(input())
A,B=map(int, input().split())

ck=A//2+B

if(ck<=N):
    print(ck)
else:
    print(N)