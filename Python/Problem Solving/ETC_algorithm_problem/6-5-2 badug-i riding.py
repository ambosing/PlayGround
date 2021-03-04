def dfs(a, b):
    global res
    if b > c:
        return
    if a == n:
        if c > b > res:
            res = b
    else:
        dfs(a + 1, b + nums[a])
        dfs(a + 1, b)


c, n = map(int, input().split())
nums = [int(input()) for _ in range(n)]
res = 0
dfs(0, 0)
print(res)
