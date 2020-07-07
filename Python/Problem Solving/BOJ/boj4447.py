for _ in range(int(input())):
    g_cnt = 0
    b_cnt = 0
    s = input()
    g_cnt = s.count("g") + s.count("G")
    b_cnt = s.count("b") + s.count("B")
    if g_cnt > b_cnt:
        print("%s is GOOD" % s)
    elif g_cnt < b_cnt:
        print("%s is A BADDY" % s)
    else:
        print("%s is NEUTRAL" % s)
