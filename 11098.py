n = int(input())
for i in range(n):
    C=[]
    name=[]
    p= int(input())
    for i in range(p):
        string=input()
        string_split=string.split()
        C.append(string_split[0])
        name.append(string_split[1])
        expensive=list(map(int,(C)))
    print(name[expensive.index(max(expensive))])