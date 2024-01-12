N= int(input())
j=0
for i in range(N*2):
    if i%2==1:
        print(str(" "*int(j))+str("*"*int(2*N-(i)))) 
        j+=1