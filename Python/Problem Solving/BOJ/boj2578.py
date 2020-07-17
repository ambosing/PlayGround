def check_num(b, a):
    for i in range(5):
        for ii in range(5):
            if b[i][ii] == a:
                b[i][ii] = 0
                return


def check_bingo(b):
    cnt = 0
    cnt += check_row_col(b)
    cnt += check_dig(b)
    return cnt


def check_row_col(b):
    cnt = 0

    for i in range(5):
        for ii in range(5):
            if b[i][ii] != 0:
                break
        else:
            cnt += 1
        for ii in range(5):
            if b[ii][i] != 0:
                break
        else:
            cnt += 1
    return cnt


def check_dig(b):
    cnt = 0
    for i in range(5):
        if b[i][i] != 0:
            break
    else:
        cnt += 1
    for i in range(5):
        if b[i][4 - i] != 0:
            break
    else:
        cnt += 1
    return cnt


def solution(b):
    res = 0
    for _ in range(5):
        nums = list(map(int, input().split()))
        for num in nums:
            check_num(b, num)
            cnt = check_bingo(b)
            res += 1
            if cnt >= 3:
                print(res)
                return


board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
solution(board)
