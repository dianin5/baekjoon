T = int(input())
for i in range(T):
    t = int(input())
    temp =0
    sum_int=0
    for i in range(t):
        score = input().split()
        C= int(score[0])
        G = float(score[1])
        temp +=round(C*G,1)
        sum_int+=C
    print(sum_int,round(temp/sum_int,1))
        