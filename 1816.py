N=int(input())
for i in range(N):
    S= int(input())
    count=0
    for j in range(2,1000000):
        if S%j ==0:
            count+=1
            break
    if count ==1:
        print("NO")
    else:
        print("YES")