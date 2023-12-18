a= int(input())
b= input()
d= 0
for i in reversed(range(3)):
    j= 2-i
    c= a*int(b[i])
    d= c*10**j+d
    print(c)
print(d)