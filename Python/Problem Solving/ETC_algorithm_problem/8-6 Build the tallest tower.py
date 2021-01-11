n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)]
dy = [0] * n
bricks.sort(key=lambda x: (x[0], x[2]), reverse=True)
dy[0] = bricks[0][1]
for i in range(1, n):
    max_val = 0
    for j in range(i - 1, -1, -1):
        if bricks[j][0] >= bricks[i][0] and bricks[j][2] >= bricks[i][2] \
                and max_val < dy[j]:
            max_val = dy[j]
    dy[i] = max_val + bricks[i][1]
print(max(dy))
