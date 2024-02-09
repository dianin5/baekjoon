S=list(input())
low = [chr(i) for i in range(97,123)]
result = [0 for i in range(len(low))]
for i in S:
    temp = low.index(i) # S에 등장하는 글자 = low의 인덱스
    result[temp]+=1
print(*result)