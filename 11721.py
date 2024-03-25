S=input()

for i in range(len(S)):
    if i!=0 and i%10==0:
        print("\n"+S[i],end='')
    else:
        print(S[i],end='')
        