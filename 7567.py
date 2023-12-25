a = input()
result = int(10)

for i in range(len(a)):
    if i >=1:
        if a[i] == a[i-1]:
            result +=5
        else:
            result +=10
print(result)