temp = []
while True:
    try:
        S = input()
        temp.append(S)
    except:
        break
result= "".join(temp).split(',')
temp2=[]
for i in result:
    temp2.append(int(i))
print(sum(temp2))