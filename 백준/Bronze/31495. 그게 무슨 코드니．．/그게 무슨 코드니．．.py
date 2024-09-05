S=input()
if S[0]!='"' or S[-1]!='"' or len(S)<3: print('CE')
else: print(S[1:-1])