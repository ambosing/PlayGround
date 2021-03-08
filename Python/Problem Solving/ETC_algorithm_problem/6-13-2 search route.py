

n, m = map(int, input().split())
b = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    b[a - 1][b - 1] = 1
