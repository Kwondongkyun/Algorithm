N=int(input())

# 소의 번호, 소의 위치
cow = {}
# 소가 길을 건너간 횟수
cnt=0

for _ in range(N):
    cow_n, cow_l = map(int, input().split())

    if cow_n in cow:
        if cow[cow_n] != cow_l:
            cnt+=1
    cow[cow_n]=cow_l

print(cnt)


