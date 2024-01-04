n= int(input())
for i in range(n):
    a,b=map(int,(input().split()))
    temp_a,temp_b =a,b
    while temp_b !=0:
        temp_a,temp_b=temp_b,temp_a%temp_b
    print((a*b)//temp_a)
    
    