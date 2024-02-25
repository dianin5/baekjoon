from collections import deque

N=deque([i for i in range(1,int(input())+1)])
for i in range(len(N)):
    if len(N)==1:
        break
    else:
        N.popleft()
        temp= N.popleft()
        N.append(temp)
        
print(*N)
