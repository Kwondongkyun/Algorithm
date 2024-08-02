import sys
input=sys.stdin.readline

K, N=map(int,input().split())
l=[int(input()) for _ in range(K)]

start=1
end=max(l)
while start<=end:
    cnt=0
    mid=(start+end)//2
    for i in l:
        cnt+=i//mid
    if cnt<N:
        end=mid-1
    else:   # cnt >= N
        start=mid+1
print(end)
