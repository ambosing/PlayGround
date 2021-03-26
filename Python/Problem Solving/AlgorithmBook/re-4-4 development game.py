def is_visit_left_side(board, y, x, d):
    if d == 0 and board[y][x - 1] == 0:
        return False
    if d == 1 and board[y + 1][x] == 0:
        return False
    if d == 2 and board[y][x + 1] == 0:
        return False
    if d == 3 and board[y - 1][x] == 0:
        return False
    return True


def game(b, y, x, d):
    


def solution():
    n, m = map(int, input().split())
    y, x, d = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
