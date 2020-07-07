while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    lst.pop(0)
    pre = ""
    for i, v in enumerate(lst):
        if v != pre:
            print(v, end=" ")
        pre = v
    print("$")
