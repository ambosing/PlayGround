def dfs(a, b, bb):
    global res
    if b > c or total - bb + b < res:
        return
    if a == n:
        if c > b > res:
            res = b
    else:
        dfs(a + 1, b + nums[a], bb + nums[a])
        dfs(a + 1, b, bb + nums[a])


c, n = map(int, input().split())
nums = [int(input()) for _ in range(n)]
total = sum(nums)
res = 0
dfs(0, 0, 0)
print(res)
