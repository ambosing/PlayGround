def dfs(a):
    global cnt, m
    if a == -1:
        return
    else:
        cnt += m // coins[a]
        m = m % coins[a]
        dfs(a - 1)


n = int(input())
coins = list(map(int, input().split()))
m = int(input())
cnt = 0
dfs(n - 1)
print(cnt)
