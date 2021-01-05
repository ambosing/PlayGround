from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_in_zero(lst):
    for i in lst:
        if 0 in i:
            return True
    return False


def bfs():
    while q:
        y, x = q.popleft()
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= xx < m and 0 <= yy < n:
                if t[yy][xx] == 0:
                    t[yy][xx] = 1
                    q.append([yy, xx])
                    v[yy][xx] = v[y][x] + 1


m, n = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and t[i][j] == 1:
            q.append([i, j])

if q:
    bfs()
    if is_in_zero(t):
        print(-1)
    else:
        res = 0
        a = False
        for i in v:
            max_val = max(i)
            if res < max_val:
                res = max_val
        print(res)
else:
    print(0)
