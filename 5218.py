T=int(input())
ans="Distances:"
for i in range(T):
    a,b=input().split()
    temp=[]
    for j in range(len(a)):
        if ord(a[j])<=ord(b[j]):
            temp.append(ord(b[j]) - ord(a[j]))
        else:
            temp.append((26+ord(b[j]))-ord(a[j]))
    print(ans,*temp)