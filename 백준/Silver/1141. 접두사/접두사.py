n=int(input())
str=[]
for i in range(n):
    a=input()
    str.append(a)

str.sort(key=len)
cnt=0

for i in range(n):
    for j in range(i+1, n):
        if str[j].startswith(str[i]):
            cnt+=1
            break
        else:
            continue
print(n-cnt)
