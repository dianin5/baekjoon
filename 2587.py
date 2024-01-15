list = []
for i in range(5):
    a = (int(input()))
    list.append(a)
list = sorted(list)
print(sum(list)//5)
print(list[2])