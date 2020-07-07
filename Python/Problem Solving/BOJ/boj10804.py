lst = [str(i + 1) for i in range(20)]
for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    limit = ((s + e) // 2 + 1) - s
    for i in range(limit):
        lst[s + i], lst[e - i] = lst[e - i], lst[s + i]
print(' '.join(lst))
