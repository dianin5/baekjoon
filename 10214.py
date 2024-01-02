Y_Score=K_Score=int(0)
T = int(input())
for i in range(T):
    for i in range(9):
        Y,K = map(int,(input().split()))
        Y_Score+=Y
        K_Score+=K
    if Y_Score> K_Score:
        print("Yonsei")
    elif Y_Score< K_Score:
        print("Korea")
    else:
        print("Draw")