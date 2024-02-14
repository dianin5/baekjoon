i=1
while True:
    a= input()
    b= input()
    if a =='END' and b=='END':
        break
    if sorted(a) == sorted(b):
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")
    i+=1