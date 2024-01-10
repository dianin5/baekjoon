# 사과
T = int(input())
result=int()
for i in range(T):
    a,b =map(int,(input().split()))
    result = result +(b%a)
print(result)