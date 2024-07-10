T=int(input()) # 테스트 케이스

for i in range(T):
    zero=1
    one=0
    N=int(input())
    for j in range(N):
        zero,one=one, zero+one
    print(zero, one)
