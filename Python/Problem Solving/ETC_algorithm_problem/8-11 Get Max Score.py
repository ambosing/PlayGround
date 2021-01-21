import sys


def dfs(s):
    for ii in range(n):
        idx = s + pt[ii][1]
        if v[ii] == 1:
            continue
        if idx <= m and dy[idx] < dy[s] + pt[ii][0]:
            v[ii] = 1
            dy[idx] = dy[s] + pt[ii][0]
            dfs(idx)
            v[ii] = 0


n, m = map(int, input().split())
pt = []
for _ in range(n):
    pt.append(list(map(int, sys.stdin.readline().split())))

dy = [-1] * (m + 1)
dy[0] = 0
v = [0] * n
dfs(0)
print(max(dy))
