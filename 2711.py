T = int(input())
for i in range(T):
    a,b = map(str,input().split())
    ai=int(a)
    temp = b[:ai-1]+b[ai:]
    print(temp)