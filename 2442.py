N = int(input())
for i in range(1,N+1):
        # 1 3 5 7 9
        print(str(" "*int(N-i))+str("*"*int(i))+(str("*")*int(i-1)))
        
    