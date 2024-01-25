import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    N =list(map(int,(sys.stdin.readline().split())))
    print(sum(N))
