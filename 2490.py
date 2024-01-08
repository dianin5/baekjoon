for i in range(3):
    Yutnori = []
    Yutnori = list(map(int,(input().split())))
    if Yutnori.count(0)==1:
        print("A")
    elif Yutnori.count(0)==2:
        print("B")
    elif Yutnori.count(0)==3:
        print("C")
    elif Yutnori.count(0)==4:
        print("D")
    elif Yutnori.count(1)==4:
        print("E")