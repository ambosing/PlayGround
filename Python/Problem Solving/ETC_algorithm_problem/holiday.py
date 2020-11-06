def dfs(a, b):
    global res, pre
    if a > n:
        if a - pre[0] <= n + 1 and b - pre[1] > res:
            res = b - pre[1]
    elif a == n:
        if b > res:
            res = b
    else:
        for i in range(a, n):
            pre[0], pre[1] = lst[i][0], lst[i][1]
            dfs(i + lst[i][0], b + lst[i][1])


n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
res = 0
pre = [0, 0]
dfs(0, 0)
print(res)
