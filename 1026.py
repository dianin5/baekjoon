T=int(input())
a=sorted(list(map(int,(input().split()))),reverse=True)
b=sorted(list(map(int,(input().split()))))
ans=0
for i in range(T):
    ans+=a[i]*b[i]
print(ans)