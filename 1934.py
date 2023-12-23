# 최소공배수
def gcd(a,b):
    if ( b ==0 ):
        return a
    else:
        return gcd(b,a%b)
    
T = int(input())

for i in range(T):
    A,B = map(int,(input().split()))
    print(A*B // gcd(A,B))

    



