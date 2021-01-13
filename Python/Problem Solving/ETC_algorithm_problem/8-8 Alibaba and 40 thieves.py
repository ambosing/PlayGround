from sys import maxsize


def dp(y, x):
    if d[y][x] != maxsize:
        return d[y][x]
    if y == 0 and x == 0:
        return b[y][x]
    elif y == 0:
        dist = dp(y, x - 1)
    elif x == 0:
        dist = dp(y - 1, x)
    else:
        dist = min(dp(y - 1, x), dp(y, x - 1))
    if dist < d[y][x]:
        d[y][x] = dist + b[y][x]
    return d[y][x]


n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
d = [[maxsize] * n for _ in range(n)]
print(dp(n - 1, n - 1))
