import sys
a,b = map(int,sys.stdin.readline().split())
if a< b:
    result =[ i for i in range(a+1,b)]
else :
    result = [i for i in range(b+1,a)]
print(len(result))
print(*result)
