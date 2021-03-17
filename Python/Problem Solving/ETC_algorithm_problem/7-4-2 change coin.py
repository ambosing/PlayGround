def dfs(a, b):
    global res
    if b > t:
        return
    elif a == k:
        if b == t:
            res += 1
    else:
        for i in range(coins[a][1] + 1):
            dfs(a + 1, b + coins[a][0] * i)


t = int(input())
k = int(input())
coins = list()
res = 0
n = 0
for _ in range(k):
    money, cnt = map(int, input().split())
    coins.append([money, cnt])
dfs(0, 0)
print(res)
