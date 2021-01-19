n = int(input())
lst = list(map(int, input().split()))
dy = [0] * n
dy[0] = lst[0]
for i in range(1, n):
    max_val = 0
    for j in range(i - 2, -1, -1):
        if max_val < dy[j]:
            max_val = dy[j]
    dy[i] = max_val + lst[i]
print(max(dy))
