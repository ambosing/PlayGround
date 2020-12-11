dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(y, x):
    global res
    if visit[y][x] == 1 or apart[y][x] == 0:
        return
    res += 1
    for idx in range(4):
        new_x = x + dx[idx]
        new_y = y + dy[idx]
        if 0 <= new_x < n and 0 <= new_y < n and apart[new_y][new_x] == 1:
            visit[y][x] = 1
            dfs(new_y, new_x)


n = int(input())
apart = [list(map(int, input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and visit[i][j] == 0:
            res = 0
            dfs(i, j)
            lst.append(res)
print(len(lst))
lst.sort()
for item in lst:
    print(item)

