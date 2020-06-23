for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = a, b
    while b > 0:
        temp = b
        b = a % b
        a = temp
    lcm = (c * d) // a
    print(lcm)
