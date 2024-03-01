cond=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
while True:
    S=input()
    count=0
    if S=='#':
        break
    for i in S:
        if i in cond:
            count+=1
    print(count)