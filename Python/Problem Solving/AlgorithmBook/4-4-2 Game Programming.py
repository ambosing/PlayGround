cnt = 1


def step_1(board, a, b, d):
    global cnt
    for _ in range(4):
        if d == 0 and board[a][b - 1] == '0':
            d = 3
            board[a][b - 1] = '1'
            cnt += 1
            step_1(board, a, b - 1, d)
        elif d == 1 and board[a - 1][b] == '0':
            d = 0
            board[a - 1][b] = '1'
            cnt += 1
            step_1(board, a - 1, b, d)
        elif d == 2 and board[a][b + 1] == '0':
            d = 1
            board[a][b + 1] = '1'
            cnt += 1
            step_1(board, a, b + 1, d)
        elif d == 3 and board[a + 1][b] == '0':
            d = 2
            board[a + 1][b] = '1'
            cnt += 1
            step_1(board, a + 1, b, d)
        d -= 1
        if d == -1:
            d = 3
    else:
        if d == 0:
            if board[a - 1][b] == '0':
                board[a - 1][b] = '1'
                cnt += 1
                step_1(board, a - 1, b, d)
        elif d == 1:
            if board[a][b - 1] == '0':
                board[a][b - 1] = '1'
                cnt += 1
                step_1(board, a, b - 1, d)
        elif d == 2:
            if board[a + 1][b] == '0':
                board[a + 1][b] = '1'
                cnt += 1
                step_1(board, a + 1, b, d)
        else:
            if board[a][b + 1] == '0':
                board[a][b + 1] = '1'
                cnt += 1
                step_1(board, a, b + 1, d)


def solution():
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())
    board = [list(input().split()) for _ in range(n)]
    board[a][b] = '1'
    step_1(board, a, b, d)
    print(cnt)


solution()
