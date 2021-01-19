n = int(input())
lst = list(map(int, input().split()))
dy = [0] * (n + 1)
dy[1] = lst[1]

for i in range(2, n + 1):
    dy[i] = max(dy[i - 1], dy[i - 2] + lst[i - 1])
print(dy[n])
