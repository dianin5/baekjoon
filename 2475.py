import sys
a = list(map(int,sys.stdin.readline().split()))
b=[i*i for i in a]
print(sum(b)%10)