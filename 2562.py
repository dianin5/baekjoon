list_a = []
for i in range(1,10):
    a = int(input())
    list_a.append(a)
print(max(list_a))
print(list_a.index(max(list_a))+1)