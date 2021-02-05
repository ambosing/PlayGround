i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    m = v // p
    n = v % p
    res = m * l
    if n > l:
        res += l
    else:
        res += n
    print("Case %d: %d" % (i, res))
