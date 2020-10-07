def dfs(a, hap, max_val):
    if hap > c:
        return
    if a == n and hap <= c:
        if max_val[0] < hap:
            max_val[0] = hap
    else:
        dfs(a + 1, hap + lst[a], max_val)
        dfs(a + 1, hap, max_val)


res = [0]
c, n = map(int, input().split())
lst = [int(input()) for _ in range(n)]
dfs(0, 0, res)
print(res[0])

