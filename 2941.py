croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
s= input()
for i in croatia:
    if i in s:
        s = s.replace(i," ")
print(len(s))