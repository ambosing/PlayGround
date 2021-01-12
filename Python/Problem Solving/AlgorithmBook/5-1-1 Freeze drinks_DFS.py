dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and not v[ny][nx] and b[ny][nx] == 0:
            v[ny][nx] = True
            dfs(ny, nx)


n, m = map(int, input().split())
b = [list(map(int, input())) for _ in range(n)]
v = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == 0 and not v[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
