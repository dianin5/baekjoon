list =[list(map(int,input().split()))for _ in range(9)]
result = max(map(max,list))

for i in range(9):
    for j in range(9):
        if list[i][j] == result:
            index= ([i+1,j+1])
print(result)
print(*index)