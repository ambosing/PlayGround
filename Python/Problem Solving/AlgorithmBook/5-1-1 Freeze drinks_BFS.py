from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x):
    q = deque([[y, x]])
    v[y][x] = True
    while q:
        y, x = q.popleft()
        for k in range(n):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0 <= ny < n and 0 <= nx < m and \
                    b[ny][nx] == 0 and not v[ny][nx]:
                q.append([ny, nx])
                v[ny][nx] = True


n, m = map(int, input().split())

b = [list(map(int, input())) for _ in range(n)]
v = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == 0 and not v[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)
