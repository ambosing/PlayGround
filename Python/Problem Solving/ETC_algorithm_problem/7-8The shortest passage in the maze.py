dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and board[new_y][new_x] == 0:
                board[new_y][new_x] = 1
                dfs(new_x, new_y)
                board[new_y][new_x] = 0


n = 7
board = [list(map(int, input().split())) for _ in range(n)]
board[0][0] = 1
cnt = 0
dfs(0, 0)
print(cnt)