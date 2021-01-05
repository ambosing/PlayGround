from collections import deque

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, 1, 1, -1]


def bfs(a, b):
    global res
    q = deque([[a, b]])
    v[a][b] = 1
    res += 1
    while q:
        y, x = q.popleft()
        for k in range(8):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= xx < n and 0 <= yy < n and v[yy][xx] == 0 and island[yy][xx] == 1:
                v[yy][xx] = 1
                q.append([yy, xx])


n = int(input())
res = 0
island = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 0 and island[i][j] == 1:
            bfs(i, j)

print(res)
