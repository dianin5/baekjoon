while True:
    list= []
    i = int(1)
    n = int(input())
    if n == -1:
        break
    for i in range(1,n//2+1):
        if n% i == 0:
            list.append(i)
    if sum(list) == n:
        print (n,"=", " + ".join(str(i) for i in list))
    else:
        print(n, "is NOT perfect.")