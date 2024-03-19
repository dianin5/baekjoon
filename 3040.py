NaN=[int(input())for _ in range(9)]
temp=[]
for i in range(9):
    for j in range(9):
        if i!=j:
            if sum(NaN)-NaN[i]-NaN[j]==100:
                temp.append(i)
                temp.append(j)
                break
NaN.pop(temp[0])
NaN.pop(temp[1]-1)
for i in NaN:
   print(i)