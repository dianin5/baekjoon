# 소음

score = int(input())
result= ""
if score>= 90 and score<=100:
    result = 'A'
elif score>=80 and score<=89:
    result = 'B'
elif score >=70 and score<=79:
    result = 'C'
elif score >=60 and score<=69:
    result = 'D'
else:
    result = 'F'
    
print(result)