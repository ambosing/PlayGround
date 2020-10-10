for _ in range(int(input())):
    a, b = map(int, input().split())
    if a % b == 0:
        c = a // b
    else:
        c = a // b + 1
    print(c ** 2)
