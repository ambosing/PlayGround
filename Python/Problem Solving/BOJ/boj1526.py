n = int(input())

for i in range(n, 0, -1):
    flag = True
    res = i
    i = str(i)
    for c in i:
        if c != "7" and c != "4":
            flag = False
            break
    if flag:
        print(res)
        break
