def dfs(a):
    if a == m:
        print(" ".join(lst))
    else:
        for i in range(n):
            if not v[i]:
                v[i] = True
                lst[a] = nums[i]
                dfs(a + 1)
                v[i] = False


n, m = map(int, input().split())
nums = [str(i + 1) for i in range(n)]
v = [False] * n
lst = ["0"] * m
dfs(0)
