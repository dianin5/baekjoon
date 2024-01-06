# 최소공배수
def gcd(a,b):
    if ( b ==0 ):
        return a
    else:
        return gcd(b,a%b)

A,B = map(int,(input().split()))
print(gcd(A,B))
print(A*B // gcd(A,B))