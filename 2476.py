
cost = []
throw = int(input())
for i in range(throw):
    a,b,c = map(int,(input().split()))
    if a==b and b==c:
        cost.append(10000+(a*1000))
    elif a==b:
        cost.append(1000+(a*100))
    elif a==c:
        cost.append(1000+(a*100))
    elif b==c:
        cost.append(1000+(b*100))
    else:
        cost.append(max(a,b,c)*100)

print(max(cost))