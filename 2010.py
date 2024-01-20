import sys

N = int(sys.stdin.readline())
com = 0
for i in range(N):
    S = int(sys.stdin.readline())
    com += S
print(com-(N-1))