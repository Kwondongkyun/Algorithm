N=int(input())
M=int(input())
S=input()

P=[0]*N
P[0]='IOI'
cnt=0

for i in range(1,N):
    P[i]=P[i-1]+'OI'
P_n=P[N-1]


for i in range(M):
    if S[i]=='I':
        if S[i:i+len(P_n)]==P_n and i+len(P_n)<=M:
            cnt+=1
        else:
            continue
    else:
        continue
print(cnt)
