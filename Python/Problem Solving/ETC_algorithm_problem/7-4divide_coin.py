from sys import maxsize


def dfs(t, a, b, c):
    global res
    if t == n:
        val = max(a, b, c) - min(a, b, c)
        if a != b and b != c and a != c and val < res:
            res = val
    else:
        dfs(t + 1, a + coins[t], b, c)
        dfs(t + 1, a, b + coins[t], c)
        dfs(t + 1, a, b, c + coins[t])


n = int(input())
coins = [int(input()) for _ in range(n)]
res = maxsize
dfs(0, 0, 0, 0)
print(res)
