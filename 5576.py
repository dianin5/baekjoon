W=[]
K=[]
for i in range(10):
    W.append(int(input()))
W=sorted(W)
temp=[]
for i in range(3):
    temp.append(W.pop())
for i in range(10):
    K.append(int(input()))
K=sorted(K)
temp2=[]
for i in range(3):
    temp2.append(K.pop())
print(sum(temp),sum(temp2))