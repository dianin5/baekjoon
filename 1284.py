while True:
    result =0 
    S = input()
    if S =='0':
        break
    for i in S:
        if i =='1':
            result+=2
        elif i =='0':
            result+=4
        else:
            result+=3
    print(int(result+(len(S)-1)+2))