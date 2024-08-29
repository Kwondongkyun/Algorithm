num=list(input())
LEN_NUM=len(num)

if LEN_NUM==2:
    A=num[0]
    B=num[1]
    print(int(A)+int(B))
elif LEN_NUM==3:
    if num[1]=='0':
        A=num[0]+num[1]
        B=num[2]
        print(int(A)+int(B))
    else:
        A=num[0]
        B=num[1]+num[2]
        print(int(A)+int(B))
else:
    A=num[0]+num[1]
    B=num[2]+num[3]
    print(int(A)+int(B))