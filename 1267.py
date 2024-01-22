import sys
N = int(sys.stdin.readline())
Y=[]
M=[]
call = list(map(int,sys.stdin.readline().split()))
for i in call:
    Y.append((i//30+1)*10)
    M.append((i//60+1)*15)
if sum(M)>sum(Y):
    print(f"Y {sum(Y)}")
elif sum(M)<sum(Y):
    print(f"M {sum(M)}")
else:
    print(f"Y M {sum(M)}")