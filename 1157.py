T=(input().upper())
cnt = [0 for _ in range(26)]
alpha= [chr(i) for i in range(65,91)]
ans=[]
for i in T:
        cnt[alpha.index(i)]+=1

if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(alpha[cnt.index((max(cnt)))])