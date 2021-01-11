def turn_left(di):
    di -= 1
    if di < 0:
        di = 3
    return di


def is_remain_left(v, r, c):
    for ii in range(c - 1, -1, -1):
        if not v[r][ii]:
            return True
    return False


def is_all_visit(v, x, y):
    for ii in range(4):
        nx = dx[ii] + x
        ny = dy[ii] + y
        if 0 <= nx <= m and 0 <= ny <= n and not v[ny][nx]:
            return False
    return True


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
y, x, d = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
v = []
for i in range(n):
    lst = []
    for j in range(m):
        if b[i][j] == 1:
            lst.append(True)
        else:
            lst.append(False)
    v.append(lst)

cnt = 0
while True:
    if is_remain_left(v, y, x):
        d = turn_left(d)
        for i in range(4):
            if d != i:
                continue
            x = dx[i] + x
            y = dy[i] + y
    elif is_all_visit(v, x, y):
        x = x - dx[d]
        y = y - dy[d]
        if b[y][x] == 1:
            break
    else:
        d = turn_left(d)
    cnt += 1
print(cnt)

