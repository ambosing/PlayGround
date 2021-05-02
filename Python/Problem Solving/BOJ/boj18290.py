dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
lst = [0] * k
v = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if lst[0] < board[i][j]:
            for t in range(4):

            lst[0] = board[i][j]
            lst.sort()
print(sum(lst))
