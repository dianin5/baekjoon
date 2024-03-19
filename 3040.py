NaN=[int(input())for _ in range(9)]
for i in range(9):
    for j in range(9):
        if i!=j:
            if sum(NaN)-NaN[i]-NaN[j]==100:
                a=i
                b=j
                break
NaN.pop(a)
NaN.pop(b)
for i in NaN:
   print(i)