N = input()
list_N=list(N)
temp= sorted(list_N, reverse=True)
int_N =int(''.join(temp))

if int_N%30 ==0:
    print(int_N)
else:
    print("-1")