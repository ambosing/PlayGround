from sys import maxsize


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global cnt
    if x == e_x and y == e_y:
        cnt += 1
    else:
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if 0 <= xx < n and 0 <= yy < n and m[y][x] < m[yy][xx]:
                chk[yy][xx] = 1
                dfs(xx, yy)
                chk[yy][xx] = 0


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
s = maxsize
e = -maxsize
cnt = 0
chk = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s > m[i][j]:
            s = m[i][j]
            s_y = i
            s_x = j
        if e < m[i][j]:
            e = m[i][j]
            e_y = i
            e_x = j
dfs(s_x, s_y)
print(cnt)

