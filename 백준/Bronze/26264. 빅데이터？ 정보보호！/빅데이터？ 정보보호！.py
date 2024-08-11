N=int(input())

s=input()

s_count=s.count("security")
b_count=s.count("bigdata")

if s_count>b_count: print("security!")
elif s_count<b_count: print("bigdata?")
else: print("bigdata? security!")