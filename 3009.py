# 네번째 점
# 세 점이 주어졌을 때 축에 평행한 직사각형을 만들기 위해 필요한 네 번째 점을 찾는 프로그램
x=0
y=0
for i in range(3):
    a, b = map(int,(input().split()))
    x^=a
    y^=b
print(x,y)
    
