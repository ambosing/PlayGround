for _ in range(int(input())):
    a, b = map(int, input().split())
    limit = a // b
    res = 1
    adder = 1
    for i in range(1, limit):
        adder += 2
        res += adder
    print(res)
