a,b = input().split()
al=[]
bl=[]
for i in a:
    al.append(i)
for i in b:
    bl.append(i)

while len(al)!=len(bl):
    if len(al)>len(bl):
        bl.insert(0,0)
    else:
        al.insert(0,0)
result=[]
for i in range(len(al)):
    result.append(int(al[i])+int(bl[i]))
print(*result,sep='')