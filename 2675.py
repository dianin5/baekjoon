T = int(input())
for i in range(T):
    a = input().split()
    a1 = int(str(a[0]))
    a2 = str(a[1])
    for i in range(len(a2)):
        print(a2[i]*a1,end='')
    print()