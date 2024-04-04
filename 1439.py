S= list(map(str,input()))
temp = []
temp.append(S[0])
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        temp.append(S[i])
count_zero=temp.count('0')
count_one=temp.count('1')
if count_zero > count_one:
    print(count_one)
elif count_zero < count_one:
    print(count_zero)
elif count_zero == count_one:
    if S.count('0')<S.count('1'):
        print(count_zero)
    elif S.count('1')<S.count('0'):
        print(count_one)