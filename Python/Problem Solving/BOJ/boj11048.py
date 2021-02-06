from collections import deque

dx = [0, 1, 1]
dy = [1, 1, 0]


def go(x, y):
    q = deque([(x, y)])
    d[y][x] = b[y][x]
    while q:
        x, y = q.popleft()
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and \
                    d[ny][nx] < d[y][x] + b[ny][nx]:
                d[ny][nx] = d[y][x] + b[ny][nx]
                q.append((nx, ny))


n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
go(0, 0)
print(d[n - 1][m - 1])
