import sys
card = [ i for i in range(1,21)]
for i in range(10):
    a,b = map(int,sys.stdin.readline().split())
    flip = card[a-1:b][::-1]
    card[a-1:b] = flip
print(*card)

