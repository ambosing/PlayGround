def dfs(a, b, c):
    global res
    if b > m:
        return
    if c == n:
        if res < a:
            res = a
    else:
        dfs(a + lst[c][0], b + lst[c][1], c + 1)
        dfs(a, b, c + 1)


n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
res = 0
dfs(0, 0, 0)
print(res)
