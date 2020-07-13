lst = [str(i + 1) for i in range(20)]

for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lim = ((a + b) // 2 + 1) - a
    for i in range(lim):
        lst[a + i], lst[b - i] = lst[b - i], lst[a + i]
print(' '.join(lst))
