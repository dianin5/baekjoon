list = []
for i in range(7):
    a = int(input())
    if a%2 ==1 :
        list.append(a)
if len(list)==0:
    print("-1")
else :
    print(sum(list))
    print(min(list))