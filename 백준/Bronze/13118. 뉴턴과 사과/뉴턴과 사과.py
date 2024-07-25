l=list(map(int, input().split()))

x,y,r=map(int, input().split())

for i in l:
    if i == x:
        print(l.index(i)+1)
        break
else:
    print(0)