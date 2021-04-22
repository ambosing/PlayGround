def dfs(a, b):
    if a == m:
        print(" ".join(lst))
    else:
        for i in range(b, n):
            lst[a] = nums[i]
            dfs(a + 1, i + 1)


n, m = map(int, input().split())
nums = [str(i + 1) for i in range(n)]
lst = ["0"] * m
dfs(0, 0)
