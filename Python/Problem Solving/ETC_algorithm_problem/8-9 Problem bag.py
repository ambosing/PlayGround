import sys

n, m = map(int, input().split())
gems = []
max_val = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    gems.append([a, b])

dy = [-1] * (m + 1)
dy[0] = 0
for i in range(m + 1):
    if dy[i] != -1:
        for gem in gems:
            if gem[0] + i <= m:
                if dy[i + gem[0]] < dy[i] + gem[1]:
                    dy[i + gem[0]] = dy[i] + gem[1]
print(max(dy))

