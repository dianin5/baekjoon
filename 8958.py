import sys
N  = int(sys.stdin.readline())
for i in range(N):
    result=count=0
    input = sys.stdin.readline()
    for i in range(len(input)):
        if input[i] =='O':
            count+=1
            result+=count
        else:
            count=0
    print(result)
