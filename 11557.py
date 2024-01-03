T = int(input())

for i in range(T):
    N = int(input())
    s_list=[]
    l_list=[]
    for i in range(N):
         S,L=map(str,(input().split()))
         s_list.append(S)
         l_list.append(L)
    litter_list = list(map(int,l_list))
    print(s_list[litter_list.index(max(litter_list))])