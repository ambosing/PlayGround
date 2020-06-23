lst = []
for _ in range(int(input())):
    lst.append(int(input()))

lst.sort()
for i in range(len(lst)):
    chk = False
    print("Pairs for %d:" % lst[i], end = "")
    for j in range(1, lst[i]):
        for k in range(j + 1, lst[i]):
            if j + k == lst[i]:
                if chk:
                    print(", %d %d" % (j, k), end="")
                else:
                    print(" %d %d" % (j, k), end="")
                chk = True
    print()
