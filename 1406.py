import sys

S=list(map(str,sys.stdin.readline().rstrip()))
T=int(sys.stdin.readline())
cursor=len(S)
right_cmd=[]
for i in range(T):
    
    cmd=list(map(str,sys.stdin.readline().split()))
    
    if cmd[0] == 'P':
        S.append(cmd[1])
        cursor+=1
    elif cmd[0] == 'L' and S:
        right_cmd.append(S.pop())
    elif cmd[0] == 'B' and S:
        S.pop()
    elif cmd[0] == 'D' and right_cmd :
        S.append(right_cmd.pop())
right_cmd.reverse()
S.extend(right_cmd)
for i in S: 
    print(i,end='')