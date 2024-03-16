S=list(map(str,input()))
alpha= [chr(i) for i in range(97,123)]
ans= [-1 for _ in range(26)]
for i in S:
        ans[alpha.index(i)]=S.index(i)
for i in ans:
    print(f"{i} ",end="")
