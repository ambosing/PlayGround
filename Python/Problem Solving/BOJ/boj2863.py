def rotate(a):
    b = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            b[i][j] = a[2 - j - 1][i]
    return b


def cal(a):
    return (a[0][0] / a[1][0]) + (a[0][1] / a[1][1])


max_val = 0
max_cnt = 0
lst = [list(map(int, input().split())) for _ in range(2)]
for cnt in range(4):
    result = cal(lst)
    lst = rotate(lst)
    if result > max_val:
        max_val = result
        max_cnt = cnt
print(max_cnt)
