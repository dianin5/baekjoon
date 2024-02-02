import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    L = list(map(int,sys.stdin.readline().split()))
    print((max(L)-min(L))*2)