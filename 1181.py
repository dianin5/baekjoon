N = int(input())
list=[]
for i in range(N):
    a = input()
    list.append((len(a),a))
temp =sorted(list, key=lambda x: (x[0],x[1]))
temp =[i[1] for i in temp]
ttemp = []
for i in temp:
    if i not in ttemp:
        ttemp.append(i)
for i in ttemp:
    print(i)