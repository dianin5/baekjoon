import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
list = []
for i in range(M,N+1):
    if i ==1:
        continue
    else:
        c=0
        for j in range(2,i):
            if i%j ==0:
                c=1
        if c==0:
            list.append(i)
if len(list) == 0:
    print("-1")
else:
    print(sum(list))
    print(min(list))