from sys import maxsize

n = int(input())
dy = [maxsize] * (n + 1)
dy[1] = 0
for i in range(1, n + 1):
    if i * 5 <= n:
        dy[i * 5] = min(dy[i * 5], dy[i] + 1)
    if i * 3 <= n:
        dy[i * 3] = min(dy[i * 3], dy[i] + 1)
    if i * 2 <= n:
        dy[i * 2] = min(dy[i * 2], dy[i] + 1)
    if i + 1 <= n:
        dy[i + 1] = min(dy[i + 1], dy[i] + 1)
print(dy[n])
