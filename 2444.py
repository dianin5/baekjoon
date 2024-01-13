N = int(input())
for i in range(1,N+1):
    print(" "*(N-i)+"*"*(i)+"*"*(i-1))
for i in range(N):
    print(" "*(i+1)+("*"*(2*N-(2*i+3))))
