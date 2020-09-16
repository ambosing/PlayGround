r, c, zr, zc = map(int, input().split())
news = [input() for _ in range(r)]
res = []

for i in range(r):
    s = ""
    for j in range(c):
        s += news[i][j] * zc
    for _ in range(zr):
        res.append(s)

for line in res:
    print(line)
