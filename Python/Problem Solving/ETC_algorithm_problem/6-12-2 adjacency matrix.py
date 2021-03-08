n, m = map(int, input().split())
b = [['0'] * n for i in range(n)]
for _ in range(m):
    y, x, d = map(int, input().split())
    b[y - 1][x - 1] = str(d)

for row in b:
    print(" ".join(row))
