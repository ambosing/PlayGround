for _ in range(int(input())):
    lst = list(input().split())
    for i in range(len(lst)):
        if i != 0:
            print(" ", end="")
        s = lst[i]
        s = s[::-1]
        print(s, end="")
    print()
