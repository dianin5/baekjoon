T = int(input())
for i in range(T):
    a = input().split()
    a1 = int(str(a[0]))
    a2 = str(a[1])
    a3 = ""
    for i in range(len(a2)):
        a3 +=a2[i]*a1
    print(a3)