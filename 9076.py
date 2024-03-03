from collections import deque
T=int(input())
for i in range(T):
    A =deque(list(map(int,input().split())))
    A=deque(sorted(A))
    A.popleft()
    A.pop()
    if A[-1]-A[0] >=4:
        print("KIN")
    else:
        print(sum(A))