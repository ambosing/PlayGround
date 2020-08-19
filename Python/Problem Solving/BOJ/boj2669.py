lists = []
max_val = 0

for i in range(4):
    lists.append(list(map(int, input().split())))
    temp = max(lists[i])
    if max_val < temp:
        max_val = temp

board = [[0] * (max_val + 1) for i in range(max_val + 1)]

for lst in lists:
    for i in range(lst[1], lst[3]):
        for j in range(lst[0], lst[2]):
            board[i][j] = 1
count = 0
for line in board:
    for item in line:
        if item == 1:
            count += 1
print(count)
