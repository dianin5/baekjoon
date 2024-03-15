
for i in range(3):
    ans=[]
    T=int(input())
    for i in range(T):
        ans.append(int(input()))
    if sum(ans) ==0:
        print("0")
    elif sum(ans) >0:
        print("+")
    else:
        print("-")