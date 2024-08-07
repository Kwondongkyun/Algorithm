# M : 사대의 수, N : 동물의 수, L : 사정거리
M, N, L = map(int, input().split())

# 사대의 위치
l_M=list(map(int, input().split()))
l_M.sort()

# 동물의 위치
l_N=[]
for i in range(N):
    x,y=map(int, input().split())
    l_N.append([x, y])

cnt=0
for x,y in l_N:
    start=0
    end=M
    while start<=end:
        mid=(start+end)//2
        check=abs(l_M[mid]-x)+y
        if check <= L:
            cnt+=1
            break
        if x>=l_M[mid]:
            start=mid+1
        else:
            end=mid-1
            
print(cnt)