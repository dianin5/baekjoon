S = input()
stack =[]
result=""
temp=""
for i in range(len(S)):
    if S[i]=='<':
        if temp:
            result+=temp[::-1]
            temp=""
        stack.append(S[i])
        result+=S[i]
    elif S[i]=='>':
        stack.pop()
        result+=S[i]
    elif len(stack)==0:
        if S[i] ==' ':
            result +=temp[::-1]+' '
            temp=""
        else:
            temp+=S[i]

    else:
        result+=S[i]
if temp:
    result+=temp[::-1]
print(result)