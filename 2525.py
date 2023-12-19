h,m = map(int,input().split())
time = int(input())
h1 = h+time//60
m1 = m+time%60
if m1>=60:
    m1-=60
    h1+=1
if h1>=24:
    h1-=24

print(h1,m1)