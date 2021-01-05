dx = [-1, 1, 0]
dy = [0, 0, 1]


def dfs(x, y):
    if y == 9:
        if la[y][x] == 2:
            print(i)
    else:
        for j in range(3):
            xx = x + dx[j]
            yy = y + dy[j]
            if 0 <= xx < 10 and v[yy][xx] == 0 and la[yy][xx] != 0:
                v[yy][xx] = 1
                dfs(xx, yy)
                break


la = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    v = [[0] * 10 for _ in range(10)]
    v[0][i] = 1
    if la[0][i] == 1:
        dfs(i, 0)
