T = int(input())

for i in range(T):
    a = input().split()
    a0 = float(str(a[0]))
    for i in range(len(a)):
        if a[i] =='@':
            a0 *= 3
        elif a[i] =='%':
            a0 += 5
        elif a[i] =='#':
            a0 -= 7
        a1 =a0
    print("{:.2f}".format(a1))
    
