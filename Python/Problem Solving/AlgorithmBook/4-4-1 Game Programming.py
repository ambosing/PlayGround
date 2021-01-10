dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def rotate_left(board, r, c):
    new_board = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new_board[j][i] = board[r][c]
    return new_board


def is_not_go(board, visit, r, c):
    for i in range(c - 1, -1, -1):
        if board[r][i] == 1 or visit[r][i]:
            return False
    return True


def make_visit(board, r, c):
    visit = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 1:
                visit[i][j] = True
    return visit


def is_all_visit(visit, r, c):
    for i in range(4):
        new_x = dx[i] + c
        new_y = dy[i] + r
        if 0 < new_x < n and 0 < new_y < m and visit[new_x][new_y]:
            return False
    return True


n, m = map(int, input().split())

y, x, d = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
v = make_visit(b, n, m)
cnt = 0
while True:
    if is_not_go(b, v, n, m):
        v = rotate_left(v, n, m)
        b = rotate_left(b, n, m)
        y, x = x, y
        d = (d + 1) % 4
        if d == 0 and y > 0 and b[y - 1][x] == 0 and not v[y - 1][x]:
            y -= 1
            v[y][x] = True
        elif d == 1 and x > 0 and b[y][x - 1] == 0 and not v[y][x - 1]:
            x -= 1
            v[y][x] = True
        elif d == 2 and y < n and b[y + 1][x] == 0 and not v[y + 1][x]:
            y += 1
            v[y][x] = True
        elif d == 3 and x < m and b[y][x + 1] == 0 and not v[y][x + 1]:
            x += 1
            v[y][x] = True
        cnt += 1
    elif is_all_visit(v, x, y):
        if d == 0 and y < n and b[y + 1][x] == 0:
            y += 1
        elif d == 1 and x < m and b[y][x + 1] == 0:
            x += 1
        elif d == 2 and y > 0 and b[y - 1][x] == 0:
            y -= 1
        elif d == 3 and x > 0 and b[y][x - 1] == 0:
            x -= 1
    else:
        v = rotate_left(v, n, m)
        b = rotate_left(b, n, m)
