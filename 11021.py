T = int(input())
c = "Case #"
d = ": "
for i in range(T):
    a,b = map(int,input().split())
    e = a+b
    print(f"{c}{i+1}{d}{e}")