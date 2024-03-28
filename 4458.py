T=int(input())
for i in range(T):
    S=list(map(str,(input())))
    S[0]=S[0].upper()
    print(''.join(S))