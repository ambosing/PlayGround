n, m = map(int, input().split())
lst = [str(i + 1) for i in range(n)]

for _ in range(m):
    i, ii = map(int, input().split())
    i -= 1
    ii -= 1
    lim = (abs(ii - i) + 1) // 2
    for j in range(lim):
        lst[i + j], lst[ii - j] = lst[ii - j], lst[i + j]
print(' '.join(lst))
