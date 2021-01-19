n = int(input())

dy = [0] * n
dy[0] = 1
dy[1] = 3
for i in range(2, n):
    dy[i] = (dy[i - 1] + dy[i - 2] * 2) % 796796
print(dy[n - 1])
