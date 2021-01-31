n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
max_val = 0

for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        sum1 += b[i][j]
        sum2 += b[j][i]
    max_val = max(sum1, max_val)
    max_val = max(sum2, max_val)
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += b[i][i]
    sum2 += b[i][n - i - 1]
max_val = max(sum1, max_val)
max_val = max(sum2, max_val)
print(max_val)
