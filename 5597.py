a=[0 for i in range(31)]
a[0]=-1
for i in range(28):
    b=int(input())
    a[b]=1

for i in range(2):
    print(a.index(0))
    a[a.index(0)]=1