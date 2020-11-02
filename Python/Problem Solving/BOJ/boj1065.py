n = int(input())

if n < 110:
    if n < 99:
        print(n)
    else:
        print(99)
else:
    cnt = 99
    for i in range(111, n + 1):
        lst = []
        lst_len = 0
        while i > 0:
            lst.append(i % 10)
            i //= 10
            lst_len += 1
        for j in range(1, lst_len - 1):
            if lst[j] + (lst[j] - lst[j - 1]) != lst[j + 1]:
                break
        else:
            cnt += 1
    print(cnt)
