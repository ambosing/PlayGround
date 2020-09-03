def rotate(nums, r, c):
    rotate_nums = [[0] * r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            rotate_nums[i][j] = nums[j][i]
    return rotate_nums


def solution():
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(sorted(list(map(int, input().split())), reverse=True))

    dic = {i: 0 for i in range(1, n + 1)}
    lst = rotate(lst, n, m)
    for i in range(m):
        max_val = max(lst[i])
        for j in range(n):
            if max_val == lst[i][j]:
                dic[j + 1] += 1
    winner_val = max(dic.values())
    winner = []
    for k, v in dic.items():
        if v == winner_val:
            winner.append(str(k))
    print(' '.join(winner))


solution()
