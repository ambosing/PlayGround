def dfs(a, b):
    global res
    if b >= res:
        return
    if a >= m:
        if a == m and b < res:
            res = b
    else:
        for i in range(n):
            dfs(a + coins[i], b + 1)


n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
res = int(1e9)
dfs(0, 0)
print(res)
