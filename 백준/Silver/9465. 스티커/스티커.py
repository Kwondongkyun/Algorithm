import sys
input=sys.stdin.readline

T=int(input())
max_list=[]

for _ in range(T):
    n=int(input())
    l=[list(map(int, input().split())) for _ in range(2)]

    if n==1:
        max_list.append(max(l[0][n-1], l[1][n-1]))
        continue
    else:
        l[0][1]+=l[1][0]
        l[1][1]+=l[0][0]

        for i in range(2,n):
            l[0][i]+=max(l[1][i-1], l[1][i-2])
            l[1][i]+=max(l[0][i-2], l[0][i-1])
        
        max_list.append(max(l[0][n-1], l[1][n-1]))
    
for i in max_list:
    print(i)