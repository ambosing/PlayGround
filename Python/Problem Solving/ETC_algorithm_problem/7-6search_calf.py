from sys import maxsize
from collections import defaultdict


def dfs(a, b):
    global res
    if a > res:
        return
    if b >= e:
        if b == e and a < res:
            res = a
    else:
        dfs(a + 1, b + 1)
        dfs(a + 1, b - 1)
        dfs(a + 1, b + 5)


s, e = map(int, input().split())
res = maxsize
dfs(0, s)
print(res)
