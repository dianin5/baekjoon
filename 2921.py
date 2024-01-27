import sys
N = int(sys.stdin.readline())
domino = []
for i in range(N+1):
    domino.append(i)
    for j in range(N+1):
        domino.append(j)
print(sum(domino))