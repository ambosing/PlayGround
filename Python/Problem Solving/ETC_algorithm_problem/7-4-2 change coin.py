def dfs(a, b):
    global res
    if b > t:
        return
    elif b == t:
        res += 1
    else:
        for i in range(a, n):
            dfs(i + 1, b + coins[i])


t = int(input())
k = int(input())
coins = list()
res = 0
n = 0
for _ in range(k):
    money, cnt = map(int, input().split())
    n += cnt
    for _ in range(cnt):
        coins.append(money)
coins.sort(reverse=True)
dfs(0, 0)
print(res)
