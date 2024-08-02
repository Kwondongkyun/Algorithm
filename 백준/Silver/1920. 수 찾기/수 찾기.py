N=int(input())
A=set(map(int, input().split()))
M=int(input())
l=list(map(int, input().split()))

for i in l:
    print(1 if i in A else 0, end=' ')