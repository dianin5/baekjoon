T= int(input())
for i in range(1,T+1):
    ans=0
    a= list(map(int,input().split()))
    a=a[1:]
    a.sort()
    for j in range(len(a)-1):
        ans = max(ans,a[j+1]-a[j])
    print(f"Class {i}")
    print(f"Max {max(a)}, Min {min(a)}, Largest gap {ans}")