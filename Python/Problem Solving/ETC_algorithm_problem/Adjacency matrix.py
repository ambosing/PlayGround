from string import ascii_lowercase

n, m = map(int, input().split())
dist = [["0"] * n for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    dist[a - 1][b - 1] = str(d)
for item in dist:
    print(" ".join(item))
