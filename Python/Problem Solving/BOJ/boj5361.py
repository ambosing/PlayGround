lst = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(int(input())):
    allPrice = 0
    lst_cnt = list(map(int, input().split()))
    for i in range(len(lst_cnt)):
        allPrice += lst_cnt[i] * lst[i]
    print("$%0.2f" % allPrice)
