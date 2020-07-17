for _ in range(int(input())):
    n = int(input())
    res = 0
    lst = [0] * (n + 1)
    for i in range(1, n + 1):
        start = 0
        while start <= n:
            lst[start] += 1
            start += i
    for i in range(1, n + 1):
        if lst[i] % 2 == 1:
            res += 1
    print(res)