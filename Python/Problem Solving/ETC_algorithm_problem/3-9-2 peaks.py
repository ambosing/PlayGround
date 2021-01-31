dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
res = 0
for y in range(n):
    for x in range(n):
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0 <= ny < n and 0 <= nx < n:
                if b[ny][nx] >= b[y][x]:
                    break
        else:
            res += 1
print(res)
