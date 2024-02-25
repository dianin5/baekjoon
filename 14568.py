N= int(input())
count=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i+j+k==N:
                if k >= j+2:
                    if i>0 and j>0 and k>0:
                        if i %2 ==0:
                            count+=1
print(count)