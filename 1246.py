import sys
N,M = map(int,sys.stdin.readline().split())
price =[int(sys.stdin.readline()) for _ in range(M)]
    
price.sort()
human=[]

for i in range(len(price)):
    count=0
    result =price[i]
    for j in price:
        if result<=j:
            count+=1
    if count > N:
        human.append(0)
    else:
        human.append(count)
final=[]
for i in range(M):
    final.append(price[i]*human[i])
print(price[final.index(max(final))],max(final))