import sys


def dfs(a, b):
    global res
    if a > res:
        return
    if b >= m:
        if b == m and a < res:
            res = a
    else:
        for i in range(n):
            dfs(a + 1, b + coins[i])


n = int(input())
coins = list(map(int, input().split()))
m = int(input())
coins.sort(reverse=True)
res = sys.maxsize
dfs(0, 0)
print(res)
