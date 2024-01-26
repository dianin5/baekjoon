import sys
import math
a,b = map(int,sys.stdin.readline().split())
for x in range(-1000,1000):
    if x*x +2*a*x == -b:
        print(x,end=' ')