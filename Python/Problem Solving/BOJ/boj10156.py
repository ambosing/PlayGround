k, n, m = map(int, input().split())

res = k * n - m
if res < 0:
    res = 0
print(res)
