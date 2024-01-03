n = int(input())
name_list=[]
dd_list=[]
mm_list=[]
yyyy_list=[]
lif=[]
for i in range(n):
    str1=input()
    input_list=str1.split()
    name=input_list[0]
    dd=int(input_list[1])
    mm=int(input_list[2])
    yyyy=int(input_list[3])
    name_list.append(name)
    dd_list.append(dd)
    mm_list.append(mm)
    yyyy_list.append(yyyy)
    life=(yyyy*365)+(mm*30)+(dd*1)
    lif.append(life)
print(name_list[lif.index(max(lif))])
print(name_list[lif.index(min(lif))])
    