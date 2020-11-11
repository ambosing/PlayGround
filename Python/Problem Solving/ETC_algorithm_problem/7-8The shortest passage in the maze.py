dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, b):
    global cnt
    for i in board:
        print(i)
    print("-----------------------------------------")
    print(y, x)
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            print(new_y, new_x)
        if 0 <= new_x < n and 0 <= new_y < n and b[new_y][new_x] == 0:
            b[new_y][new_x] = 1
            dfs(new_x, new_y, b)
            b[new_y][new_x] = 0


n = 7
board = [list(map(int, input().split())) for _ in range(n)]
board[0][0] = 1
cnt = 0
dfs(0, 0, board)
print(cnt)
