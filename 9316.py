T=int(input())
for i in range(T):
    ans=[]
    a = list(map(int,input().split()))
    for i in a:
        if i%2==0:
            ans.append(i)
    print(sum(ans),min(ans))