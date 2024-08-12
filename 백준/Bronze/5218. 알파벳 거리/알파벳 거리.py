n=int(input())

for i in range(n):
    a,b=input().split()
    print('Distances: ', end='')
    for j in range(len(a)):
        if a[j]<=b[j]:
            print(ord(b[j])-ord(a[j]), end=' ')
        else:
            print(ord(b[j])+26-ord(a[j]), end=' ')
    print()