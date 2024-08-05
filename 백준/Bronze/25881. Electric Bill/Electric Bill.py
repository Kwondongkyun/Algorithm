a,b=map(int,input().split())
n=int(input())

for i in range(n):
    k=int(input())
    if k<=1000:
        print(k, k*a)
    else:
        print(k, 1000*a+(k-1000)*b)