def dfs(a):
    if a == m:
        print(" ".join(lst))
        return
    for i in range(n):
        lst[a] = nums[i]
        dfs(a + 1)


n, m = map(int, input().split())
nums = [str(i + 1) for i in range(n)]
lst = ["0"] * m
dfs(0)
