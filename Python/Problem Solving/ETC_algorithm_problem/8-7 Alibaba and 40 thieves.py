from collections import deque
from sys import maxsize

dx = [1, 0]
dy = [0, 1]


def bfs():
    d[0][0] = b[0][0]
    q = deque([[0, 0]])
    while q:
        y, x = q.popleft()
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < n and nx < n:
                dist = d[y][x] + b[ny][nx]
                if d[ny][nx] > dist:
                    d[ny][nx] = dist
                    q.append([ny, nx])
    return d[n - 1][n - 1]


n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
d = [[maxsize] * n for _ in range(n)]
print(bfs())
