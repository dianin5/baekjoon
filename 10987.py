S=list(input())
sl = ['a','e','i','o','u']
count=0
for i in range(len(S)):
    if S[i] in sl:
        count+=1
print(count)