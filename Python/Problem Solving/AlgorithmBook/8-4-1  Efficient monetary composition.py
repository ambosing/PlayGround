from sys import maxsize

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

dy = [maxsize] * (m + 1)
dy[0] = 0
for i in range(m + 1):
    for a in lst:
        if dy[i] != maxsize and i + a <= m:
            dy[i + a] = min(dy[i] + 1, dy[i + a])

if dy[m] == maxsize:
    print(-1)
else:
    print(dy[m])
print(dy)