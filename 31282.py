import sys
N,M,K =map(int,(sys.stdin.readline().split()))
count =0
M1 = N
K1 = 0
while K1<M1:
    M1 +=M
    K1 +=K
    count +=1
print(count)

# import math
# N, M, K = map(int, input().split())
# count = math.ceil(N / (K - M))
# print(count)