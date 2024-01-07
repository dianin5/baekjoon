# 피보나치
n = int(input())
def fib(n):
    result = []
    a,b=1,1
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result[-1]
print(fib(n))
