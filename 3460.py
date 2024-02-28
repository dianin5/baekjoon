T= int(input())
for i in range(T):
    N= list(bin(int(input())))
    N.reverse()
    ans=[]
    x='1'
    for i in range(len(N)):
        if N[i]==x:
            ans.append(i)
    print(*ans)