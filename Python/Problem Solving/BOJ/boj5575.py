for _ in range(3):
    hms = (list(map(int, input().split())))
    h = hms[3] - hms[0]
    m = hms[4] - hms[1]
    s = hms[5] - hms[2]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
    print(h, m, s)
