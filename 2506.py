import sys
N = int(sys.stdin.readline())
ox= list(map(int,sys.stdin.readline().split()))
result = []
O=0
for i in range(len(ox)):
    if ox[i]==1:
        O+=1
        result.append(O)
    else:
        O=0
        result.append(0)
print(sum(result))