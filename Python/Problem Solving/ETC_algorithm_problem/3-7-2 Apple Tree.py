n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
n2 = n // 2
s = n // 2
e = n // 2
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res += b[i][j]
    if i < n2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
