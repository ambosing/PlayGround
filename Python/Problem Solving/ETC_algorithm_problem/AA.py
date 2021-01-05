from collections import deque

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]


def bfs(a, b):
    q = deque([[a, b]])
    v[a][b] = 1
    while q:
        y, x = q.popleft()
        for c in range(4):
            yy = y + dy[c]
            xx = x + dx[c]
            if 0 <= xx < n and 0 <= yy < n:
                if v[yy][xx] == 0 and h[yy][xx] > i:
                    v[yy][xx] = 1
                    q.append([yy, xx])


n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(1, 100):
    cnt = 0
    v = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if v[j][k] == 0 and h[j][k] > i:
                bfs(j, k)
                cnt += 1
    if cnt > res:
        res = cnt
print(res)
