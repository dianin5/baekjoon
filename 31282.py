import sys
N,M,K =map(int,(sys.stdin.readline().split()))
count =0
while True :
    if N+(count*M) <= count*K:
        print(count)
        break
    else:
        count+=1