T=int(input())
alpha=[chr(i) for i in range(65,91)]
for i in range(T):
    a=list(input())
    temp=[x for x in alpha if x not in a]
    ans=0
    for i in temp:
        ans+=ord(i)
    print(ans)
        
    