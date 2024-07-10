N, K=map(int, input().split()) # N : 물품 수, K : 버틸 무게

w=[]
v=[]
cost=[0]*(K+1)
for i in range(N):
    W, V = map(int, input().split()) # W : 물건 무게, V : 물건의 가치
    w.append(W)
    v.append(V)

for i in range(N):
    for j in range(K, w[i]-1,-1):
        cost[j]=max(cost[j], cost[j-w[i]]+v[i])
print(max(cost))