import sys
temp = []
for i in range(4):
    a,b = map(int,sys.stdin.readline().split())
    if i>=1:
        temp.append((temp[i-1]+b)-a)
    else:
        temp.append(b-a)
print(max(temp))
