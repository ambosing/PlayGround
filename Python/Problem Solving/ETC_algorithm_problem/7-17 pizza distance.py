from sys import maxsize
from itertools import combinations


def dfs():
    global res
    for lst in combinations(p, m):
        d = [101] * len(pp)
        for r1, r2 in lst:
            for idx, (v1, v2) in enumerate(pp):
                dist = abs(v1 - r1) + abs(v2 - r2)
                if d[idx] > dist:
                    d[idx] = dist
        if sum(d) < res:
            res = sum(d)


n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
p = []
pp = []
for i in range(n):
    for j in range(n):
        if b[i][j] == 2:
            p.append([i, j])
        elif b[i][j] == 1:
            pp.append([i, j])
res = maxsize
dfs()
print(res)
