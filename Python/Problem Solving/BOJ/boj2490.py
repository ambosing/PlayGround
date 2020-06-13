for i in range(3):
    lst = map(int, input().split())
    lstSum = sum(lst)
    if lstSum == 0:
        print("D")
    elif lstSum == 1:
        print("C")
    elif lstSum == 2:
        print("B")
    elif lstSum == 3:
        print("A")
    else:
        print("E")
