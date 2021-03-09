def dfs(a, b):
    global res
    if a > m:
        return
    if res < b:
        res = b
    for i in range(n):
        if not used[i]:
            used[i] = True
            dfs(a + info[i][1], b + info[i][0])
            used[i] = False


n, m = map(int, input().split())
res = 0
info = []
for _ in range(n):
    score, time = map(int, input().split())
    info.append([score, time])
used = [False] * n
dfs(0, 0)
print(res)
