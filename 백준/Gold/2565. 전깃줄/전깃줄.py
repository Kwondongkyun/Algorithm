N=int(input())

lst=[]
dp=[1]*N
for i in range(N):
    a,b=map(int, input().split())
    lst.append([a,b])

lst.sort(key=lambda x:x[0])
cnt=0
for i in range(1, N):
    for j in range(i):
        if lst[j][1]<lst[i][1]:
            dp[i]=max(dp[i], dp[j]+1)
            
print(N-max(dp))