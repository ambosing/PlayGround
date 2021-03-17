def dfs(d, a, b, c):
    global res
    if d == n:
        if a == b or a == c or b == c:
            return
        min_val = min(a, b, c)
        max_val = max(a, b, c)
        diff = max_val - min_val
        if diff < res:
            res = diff
    else:
        dfs(d + 1, a + coins[d], b, c)
        dfs(d + 1, a, b + coins[d], c)
        dfs(d + 1, a, b, c + coins[d])


n = int(input())
coins = []
res = int(1e9)
for _ in range(n):
    coins.append(int(input()))
dfs(0, 0, 0, 0)
print(res)
