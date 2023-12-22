# 소인수분해
# 첫째줄에 입력값을 받고 2부터 입력값에 나누고 오름차순으로 정렬한다.

N = int(input())
a = int(2)
c= N//a
while a <= N:
    if N%a ==0:
        print(a)
        N = N//a
    else:
        a+=1

    
    