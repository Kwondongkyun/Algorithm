T=int(input())
for _ in range(T):
    a,b=map(str, input().split())
    a_l=list(a)
    b_l=list(b)
    if sorted(a_l)==sorted(b_l):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")