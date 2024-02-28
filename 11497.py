T = int(input())
for i in range(T):
    a = int(input())
    N= list(map(int,input().split()))
    N.sort(reverse=True)
    temp = N
    result= []
    for i in range(len(temp)):
        if i%2 ==0:
            result.insert(0,temp[i])
        else:
            result.append(temp[i])
    sub=[]
    for i in range(1,len(result)):
        sub.append(abs(result[i]-result[i-1]))
    sub.append(abs(result[0]-result[-1]))
    print(max(sub))