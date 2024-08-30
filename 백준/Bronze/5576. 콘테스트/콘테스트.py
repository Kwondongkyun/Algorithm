K=[]
W=[]

for i in range(20):
    n=int(input())
    if i<10:
        K.append(n)
    else:
        W.append(n)
K.sort()
W.sort()
K=K[7:]
W=W[7:]

print(sum(K), sum(W))