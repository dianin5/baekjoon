X= int(input())
T = int(input())
cost =[]
for i in range(T):
    a,b = map(int,input().split())
    cost.append(a*b)
if X == sum(cost):
    print("Yes")
else:
    print("No")