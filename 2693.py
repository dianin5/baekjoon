T=int(input())
for i in range(T):
    xl=list(map(int,input().split()))
    xl.sort()
    print(min(xl[7:10]))