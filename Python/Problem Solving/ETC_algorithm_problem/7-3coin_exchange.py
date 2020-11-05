def dfs(a, b):
    global res
    if b > t:
        return
    if a == k:
        if b == t:
            res += 1
    else:
        for i in range(coins[a][1]):
            dfs(a + 1, b + coins[a][0] * i)


t = int(input())
k = int(input())
coins = []
for _ in range(k):
    coin, cnt = map(int, input().split())
    coins.append([coin, cnt + 1])
res = 0
dfs(0, 0)
print(res)
