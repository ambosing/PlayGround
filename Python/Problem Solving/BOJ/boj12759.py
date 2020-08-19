def check(lst, num):
    for i in range(1, 4):
        chk = [True] * 2
        for j in range(1, 4):
            if lst[i][j] != num:
                chk[0] = False
            if lst[j][i] != num:
                chk[1] = False
        if chk[0] or chk[1]:
            return num
    chk = [True] * 2
    for i in range(1, 4):
        if lst[i][i] != num:
            chk[0] = False
        if lst[i][4 - i] != num:
            chk[1] = False
    if chk[0] or chk[1]:
        return num
    return 0


n = int(input())

board = [[0] * 4 for i in range(4)]
for i in range(9):
    y, x = map(int, input().split())
    board[y][x] = n
    result = check(board, n)
    if result != 0:
        print(result)
        print(board)
        break
    if n == 2:
        n = 1
    elif n == 1:
        n = 2
else:
    print(0)
