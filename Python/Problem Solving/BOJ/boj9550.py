for _ in range(int(input())):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    for i in lst:
        result += i // b
    print(result)
