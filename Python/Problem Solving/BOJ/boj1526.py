n = int(input())

for i in range(n, 0, -1):
    flag = True
    res = i
    while i > 0:
        ii = i % 10
        if ii != 4 and ii != 7:
            flag = False
            break
        i //= 10
    if flag:
        print(res)
        break
