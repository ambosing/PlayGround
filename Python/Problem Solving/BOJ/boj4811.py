import sys


def go(dy, f, h):
    if dy[f][h] != 0:
        return dy[f][h]
    if f == 0:
        return 1
    if h == 0:
        dy[f][h] = go(dy, f - 1, h + 1)
        return dy[f][h]
    dy[f][h] = go(dy, f - 1, h + 1) + go(dy, f, h - 1)
    return dy[f][h]


dy = [[0] * 1001 for _ in range(1001)]
while True:
    n = int(input())
    if n == 0:
        break
    print(go(dy, n, 0))
