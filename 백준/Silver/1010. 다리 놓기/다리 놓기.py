T=int(input())

def fact(x):
    t=1
    for i in range(1, x+1):
        t*=i
    return t

def bridge(x,y):
    return int(fact(y)/(fact(x)*fact(y-x)))

for i in range(T):
    N,M=map(int, input().split())
    print(bridge(N,M))