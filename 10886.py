N = int(input())
yes =int()
no = int()
for i in range(N):
    a = int(input())
    if a ==1:
        yes+=1
    elif a ==0:
        no+=1
    
if yes<no :
    print("Junhee is not cute!")
elif yes>no:
    print("Junhee is cute!")
    