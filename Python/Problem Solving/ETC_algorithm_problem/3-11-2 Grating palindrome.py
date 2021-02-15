n = 7
b = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(3):
        p1 = b[i][j:j + 5]
        if p1 == p1[::-1]:
            cnt += 1
for i in range(n):
    for j in range(3):
        p2 = []
        for k in range(j, j + 5):
            p2.append(b[k][i])
        if p2 == p2[::-1]:
            cnt += 1
print(cnt)

