import sys

N = int(sys.stdin.readline())
Nl=[0]*10001

for i in range(N):
    Nl[int(sys.stdin.readline())]+=1
for i in range(10001):
    if Nl!=0:
        for j in range(Nl[i]):
            print(i)