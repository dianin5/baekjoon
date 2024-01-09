list_i=[]
for i in range(10):
    N= int(input())
    list_i.append(N)
result=list_i[0]
for i in range(1,10):
    result-=list_i[i]
print(result)