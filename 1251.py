s = input()
a=b=c=""
result=[]
for i in range(1,len(s)):
    a=s[:i]
    a_list=list(a)
    a_list.reverse()
    new_s=s[i:]
    for j in range(1,len(new_s)):
        b=new_s[:j]
        b_list=list(b)
        b_list.reverse()
        c=new_s[j:]
        c_list=list(c)
        c_list.reverse()
        result.append("".join(a_list)+"".join(b_list)+"".join(c_list))
result.sort()
print(result[0])