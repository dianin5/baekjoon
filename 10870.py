N= int(input())
count=[]
for i in range(N+1):
    if i ==0:
        count.append(0)
    elif i==1:
        count.append(1)
    elif i==2:
        count.append(1)
    else:
        count.append(count[i-2]+count[i-1])
print(count[N])