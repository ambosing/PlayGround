from sys import maxsize

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(y, x, cnt):
    global res
    if x == m - 1 and y == n - 1:
        if cnt < res:
            res = cnt
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                dfs(ny, nx, cnt + 1)
                maze[ny][nx] = 1


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
res = maxsize
dfs(0, 0, 1)
print(res)
