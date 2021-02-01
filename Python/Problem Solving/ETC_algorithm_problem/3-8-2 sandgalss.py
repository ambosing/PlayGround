def rotate(board, r, d, t):
    r -= 1
    if d == 0:
        for i in range(t):
            num = board[r].pop(0)
            board[r].append(num)
    else:
        for i in range(t):
            num = board[r].pop()
            board[r].insert(0, num)


n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
n2 = n // 2
s = 0
e = n
res = 0
for _ in range(m):
    rotate(b, *map(int, input().split()))
for j in range(n):
    res += sum(b[j][s:e])
    if j < n2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)

