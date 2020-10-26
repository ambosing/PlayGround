while True:
    try:
        n, b, m = map(float, input().split())
    except:
        break
    i = 0
    while n < m:
        i += 1
        n = (1 + 0.01 * b) * n
    print(i)
