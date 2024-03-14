N = int(input())
ans =[]
for i in range(1,N+1):
    if i %2 ==0:
        ans.append("CY")
    else:
        ans.append("SK")
print(ans[-1])