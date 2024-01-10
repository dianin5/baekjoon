def fel(T,leng):
    a = str(T).rjust(leng,'0')
    b =''.join(list(reversed(a)))
    if len(str(a))==leng:
        if a ==b:
            return True
        else:
            return False
    
while True:
    T = input()
    if T =='0':
        break
    else :
        temp = int(T)
        leng = len(T)
        for i in range(999999999):
            if fel(temp+i,leng):
                print(i)
                break