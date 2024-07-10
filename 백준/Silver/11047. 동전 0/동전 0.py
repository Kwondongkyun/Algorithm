n,k=map(int, input().split())
l=[]*n
count=0

for i in range(n):
    l.append(int(input()))
l.reverse()

for coin in l:
    count+=k//coin
    k%=coin

print(count)
