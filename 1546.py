import sys
N = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))
m = max(score)
result=[]
for i in range(N):
    result.append(score[i] /m *100)
print(sum(result)/len(result))