import sys
T = int(sys.stdin.readline())
result=[]
for i in range(T):
    result.append(list(map(int,sys.stdin.readline().split())))
result=sorted(result)
for i in range(T):
    print(*result[i])