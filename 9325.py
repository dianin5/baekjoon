T = int(input())
for i in range(T):
    result=0
    s = int(input())
    n = int(input())
    for i in range(n):
        p,q = map(int,(input().split()))
        result+=p*q
    print(s+result)