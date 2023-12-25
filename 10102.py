V = int(input())
a = input()
a_count =int()
b_count = int()
for i in range(V):
    if a[i] =='A':
        a_count+=1
    else:
        b_count+=1

if a_count>b_count:
    print('A')
elif a_count<b_count:
    print('B')
else:
    print('Tie')