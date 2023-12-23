a,b,c = map(int,(input().split()))
cost = int()

for i in range(3):
    if a==b and b==c:
        cost = 10000+(a*1000)
    elif a==b:
        cost =1000+(a*100)
    elif a==c:
        cost =1000+(a*100)
    elif b==c:
        cost = 1000+(b*100)
    else:
        cost = max(a,b,c)*100
        
print(cost)