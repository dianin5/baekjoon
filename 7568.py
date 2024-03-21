T=int(input())
temp=[1 for _ in range(T)]
kg_temp=[]
cm_temp=[]
for i in range(T):
    kg,cm=map(int,input().split())
    kg_temp.append(kg)
    cm_temp.append(cm)
for i in range(T):
    for j in range(T):
        if kg_temp[i]<kg_temp[j] and cm_temp[i]<cm_temp[j]:
            temp[i]+=1
print(*temp)