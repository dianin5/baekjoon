M = int(input())
N = int(input())
result= []
for i in range(1,101):
    perfect = i*i
    if perfect>=M and perfect<=N:
        result.append(perfect)
if len(result) ==0:
    print(-1)
elif len(result) !=0:
    print(sum(result))
    print(min(result))