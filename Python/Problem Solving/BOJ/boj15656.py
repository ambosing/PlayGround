def dfs(a):
    if a == m:
        print(" ".join(lst))
        return
    for i in range(n):
        lst[a] = nums[i]
        dfs(a + 1)


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
nums = list(map(str, nums))
lst = ["0"] * m
dfs(0)
