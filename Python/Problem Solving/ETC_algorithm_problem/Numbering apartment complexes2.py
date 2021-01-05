from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(a, b):
    q = deque([[a, b]])
    ans = 0
    visited[a][b] = 1
    while q:
        y, x = q.popleft()
        ans += 1
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= xx < n and 0 <= yy < n and apart[yy][xx] == 1 and visited[yy][xx] == 0:
                visited[yy][xx] = 1
                q.append([yy, xx])
    return ans


n = int(input())
apart = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and apart[i][j] == 1:
            lst.append(bfs(i, j))

lst.sort()
print(len(lst))
for i in lst:
    print(i)
