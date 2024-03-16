T=int(input())
for i in range(T):
    P,M=map(int,input().split())
    count=0
    ans = [0 for _ in range(M+1)]
    for j in range(P):
        a= int(input())
        if ans[a]==0:
            ans[a]=a
        else:
            count+=1
    print(count)