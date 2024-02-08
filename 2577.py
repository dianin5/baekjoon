A= int(input())
B= int(input())
C= int(input())
l2= list(str(A*B*C))
for i in range(10):
    print(l2.count(str(i)))