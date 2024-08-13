M, N = map(int, input().split())

prime=[True]*(N+1)

prime[0]=False
prime[1]=False
cnt=0

for i in range(2, N+1):
    if prime[i]:
        for j in range(i+i, N+1, i):
            prime[j]=False

for i in range(M, N+1):
    if prime[i]:
        print(i)