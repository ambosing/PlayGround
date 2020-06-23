for _ in range(int(input())):
    a, b = map(int, input().split())
    result = a // b
    if a % b != 0:
        result += 1
    print(result)
