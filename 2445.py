N= int(input())
for i in range(1,N+1):
    print("*"*(i)+" "*(N*2-(i+i))+"*"*(i))
for i in range(1,N):
    print("*"*(N-i)+" "*(i+i)+"*"*(N-i))