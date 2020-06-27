while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if c - b == b - a:
        d = c + (b - a)
        print("AP %d" % d)
    else:
        if a != 0:
            d = c * (b // a)
        elif a == 0:
            d = c * (c // b)
        print("GP %d" % d)
