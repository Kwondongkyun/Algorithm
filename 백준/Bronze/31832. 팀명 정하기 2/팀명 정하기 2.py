N=int(input())

for _ in range(N):
    S=input()
    if len(S)>10:
        continue
    upper=0
    lower=0

    for s in S:
        if s=='-':
            continue
        if not s.isdecimal() and s.isupper():
            upper+=1
        elif not s.isdecimal() and s.islower():
            lower+=1
    if upper>lower:
        continue
    if S.isdecimal():
        continue
    print(S)