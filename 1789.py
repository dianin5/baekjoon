# 수들의 합
#서도 다른 N개의 자연수의 합이 S라고 한다. S를 알 때 자연수 N의 최대 값은?
S = int(input())
b= int()
list = []
for i in range(S):
    b= b+i+1
    if b>S:
        break
    list.append(b)
    
print(len(list))
