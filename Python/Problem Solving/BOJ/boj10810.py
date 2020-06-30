n, m = map(int, input().split())
lst = ["0"] * n

for _ in range(m):
    a, b, c = map(int, input().split())
    s = min(a, b)
    e = max(a, b)
    for i in range(s - 1, e):
        lst[i] = str(c)
print(' '.join(lst))
