from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = 7
board = [list(map(int, input().split())) for _ in range(n)]
board[0][0] = 1
dis = [[0] * n for _ in range(n)]
deq = deque([(0, 0)])
while deq:
    x, y = deq.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and board[new_y][new_x] == 0:
            board[new_y][new_x] = 1
            deq.append((new_x, new_y))
            dis[new_y][new_x] = dis[y][x] + 1

for i in dis:
    print(i)
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
