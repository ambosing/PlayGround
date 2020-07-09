for i in range(int(input())):
    lst = list(input().split())
    if lst[1] == "+":
        if int(lst[0]) + int(lst[2]) == int(lst[-1]):
            print("Case %d: YES" % (i + 1))
        else:
            print("Case %d: NO" % (i + 1))
    elif lst[1] == "-":
        if int(lst[0]) - int(lst[2]) == int(lst[-1]):
            print("Case %d: YES" % (i + 1))
        else:
            print("Case %d: NO" % (i + 1))
