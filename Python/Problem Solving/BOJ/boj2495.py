for i in range(3):
    cnt = 0
    max_cnt = 0
    pre = '0'
    s = input()
    for c in s:
        if pre != c:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
        pre = c
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
    print(max_cnt)
