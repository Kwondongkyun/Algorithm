T=int(input())
N=int(input())
l=list(map(int, input().split()))

if(sum(l)>=T): print('Padaeng_i Happy')
else: print('Padaeng_i Cry')