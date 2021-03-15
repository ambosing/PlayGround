def dfs(a):
    global res
    if a > t:
        return
    elif a == t:
        res += 1
    else:



t = int(input())
k = int(input())
coins = list()
res = 0
for _ in range(k):
    money, cnt = map(int, input().split())
    for _ in range(cnt):
        coins.append(money)
coins.sort(reverse=True)


