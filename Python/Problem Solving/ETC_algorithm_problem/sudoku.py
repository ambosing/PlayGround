def check_visit(v):
    for item in v:
        if item == 0:
            return False
    return True


def check_row(lists, i):
    visit = [0] * 9
    for j in range(9):
        idx = lists[i][j] - 1
        visit[idx] += 1
    if not check_visit(visit):
        return True
    return False


def check_col(lists, i):
    visit = [0] * 9
    for j in range(9):
        idx = lists[j][i] - 1
        visit[idx] += 1
    if not check_visit(visit):
        return True
    return False


def check_block(lists, s1, s2):
    board_start = [0, 3, 6]
    visit = [0] * 9
    for j in range(3):
        s_j = board_start[s1]
        s_k = board_start[s2]
        for k in range(3):
            idx = lists[s_j + j][s_k + k] - 1
            visit[idx] += 1
    if not check_visit(visit):
        return True
    return False


def solution(lst):
    for i in range(9):
        if check_row(lst, i) or check_row(lst, i):
            print("NO")
            return
    for i in range(3):
        for ii in range(3):
            if check_block(lst, i, ii):
                print("NO")
                return
    else:
        print("YES")


lists = list()
for _ in range(9):
    lists.append(list(map(int, input().split())))
solution(lists)

