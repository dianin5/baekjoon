ans = [i for i in range(1,9)]
re_ans =sorted(ans,reverse=True)
mel = list(map(int,input().split()))
if ans == mel:
    print('ascending')
elif re_ans == mel:
    print('descending')
else:
    print('mixed')