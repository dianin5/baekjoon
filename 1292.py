a,b=map(int,input().split())
ans=[]
for i in range(1,b+1):
    if i ==1:
        ans.append(1)
    else:
        for j in range(i):
            ans.append(i)
print(sum(ans[a-1:b]))