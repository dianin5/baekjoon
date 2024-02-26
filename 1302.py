T = int(input())
book=[]
for i in range(T):
    book.append(input())
book.sort()
print(max(book, key=book.count))