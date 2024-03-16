N=int(input())
temp=1
for i in range(1,N+1):
    temp*=i
str=str(temp)
ans=list(str)
ans.reverse()
count=0
for i in ans:
    
    if i=='0':
        count+=1
    else:
        break
print(count) 