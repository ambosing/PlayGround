from collections import deque


n = int(input())
farm = []
for _ in range(n):
    farm.append(list(map(int, input().split())))
s = n // 2
deq = deque([[s, s]])
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
res = farm[s][s]
chk = [[0] * n for _ in range(n)]
chk[s][s] = 1
a = 0
while a < s:
    size = len(deq)
    for j in range(size):
        y, x = deq.popleft()
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if chk[new_y][new_x] == 0:
                deq.append([new_y, new_x])
                chk[new_y][new_x] = 1
                res += farm[new_y][new_x]
    a += 1
print(res)
