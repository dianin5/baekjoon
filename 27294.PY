T,S=map(int,input().split())
BOBR=0
if T<=11:
    BOBR=280
elif T<=16:
    if S ==1:
        BOBR=280
    else:
        BOBR=320
else:
    BOBR=280
print(BOBR)