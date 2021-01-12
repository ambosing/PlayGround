from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(y, x):
    q = deque([[y, x]])
    d[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1 and d[ny][nx] == 0:
                d[ny][nx] = d[y][x] + 1
                q.append([ny, nx])


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
bfs(0, 0)
print(d[n - 1][m - 1])
