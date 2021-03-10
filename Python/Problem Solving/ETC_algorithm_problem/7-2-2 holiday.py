def dfs(a, b):
    global res
    if a > n + 1:
        return
    if res < b:
        res = b
    for i in range(a, n + 1):
        dfs(i + lst[i][0], b + lst[i][1])


n = int(input())
lst = [[0, 0]]
res = 0
for _ in range(n):
    t, p = map(int, input().split())
    lst.append([t, p])
dfs(1, 0)
print(res)
