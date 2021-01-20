from sys import maxsize

n = int(input())
coins = list(map(int, input().split()))
m = int(input())

dy = [maxsize] * (m + 1)
dy[0] = 0
for i in range(m + 1):
    if dy[i] != maxsize:
        for coin in coins:
            if i + coin <= m and dy[i + coin] > dy[i] + 1:
                dy[i + coin] = dy[i] + 1
print(dy[m])
