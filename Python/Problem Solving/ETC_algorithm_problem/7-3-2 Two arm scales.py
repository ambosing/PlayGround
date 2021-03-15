def dfs(a, b):
    if a == n:
        if 0 < b <= hap:
            res.add(b)
    else:
        dfs(a + 1, b + lst[a])
        dfs(a + 1, b - lst[a])
        dfs(a + 1, b)


n = int(input())
lst = list(map(int, input().split()))
res = set()
hap = sum(lst)
dfs(0, 0)
print(hap - len(res))
