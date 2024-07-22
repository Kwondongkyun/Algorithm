N = int(input())
l = list(map(int, input().split()))
result=[]
l_sort = sorted(set(l))

dict = {idx: value for value, idx in enumerate(l_sort)}

for i in l:
    result.append(dict[i])

for i in range(len(result)):
    print(result[i], end=' ')