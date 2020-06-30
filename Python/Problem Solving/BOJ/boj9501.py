for _ in range(int(input())):
    n, d = map(int, input().split())
    cnt = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a * (b / c) >= d:
            cnt += 1
    print(cnt)