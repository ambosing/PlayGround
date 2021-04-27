def dfs(a):
    if a == m:
        print(" ".join(lst))
        return
    for i in range(n):
        if not v[i]:
            v[i] = True
            lst[a] = nums[i]
            dfs(a + 1)
            v[i] = False


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
nums = list(map(str, nums))
lst = ["0"] * m
v = [False] * n
dfs(0)
