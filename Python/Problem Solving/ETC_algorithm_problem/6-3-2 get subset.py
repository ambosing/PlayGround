def dfs(a):
    if a == n:
        lst = []
        for i in range(n):
            if v[i]:
                lst.append(str(nums[i]))
        print(' '.join(lst))
    else:
        dfs(a + 1)
        v[a] = False
        dfs(a + 1)
        v[a] = True


n = int(input())
nums = [i for i in range(1, n + 1)]
v = [True] * n
dfs(0)
