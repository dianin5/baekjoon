import sys

def binary_search(al,i):
    start, end = 0, len(al)-1
    while start<=end:
        mid = (start+end)//2
        if al[mid]==i:
            return True
        elif al[mid]>i:
            end=mid-1
        else:
            start = mid+1
    return False

while True:

    a,b = map(int,(sys.stdin.readline().split()))
    if a==0 and b==0:
        break
    al = [int(sys.stdin.readline()) for i in range(a)]
    bl = [int(sys.stdin.readline()) for i in range(b)]
    count=0
    for i in bl:
        if binary_search(al,i):
            count +=1
    print(count)