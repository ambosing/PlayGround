def dfs(a, num_sum, num_sum_rev):
    if a >= n:
        return
    for i in range(a, n):
        v[nums[i] - 1] = True
        v[num_sum_rev - nums[i] - 1] = True
        dfs(i + 1, num_sum + nums[i], num_sum_rev - nums[i])


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
hap = sum(nums)
v = [False] * hap
v[hap - 1] = True
dfs(0, 0, hap)
print(v.count(False))
