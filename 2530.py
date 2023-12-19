h,m,s = map(int,input().split())
time = int(input())

total = h*3600+m*60+s+time
h1 = total//3600
h2 = total%3600
m1 = h2//60
s1 = h2%60
if h1 >=24:
    h1= h1 %24

print(h1,m1,s1)