n, m = map(int, input().split())
lst = []
cnt = 0
for _ in range(n):
    p, t = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if p - t < 0:
        pt = 0
        lst.append(1)
    else:
        pt = p - t
        lst.append(a[pt])
lst.sort()
for item in lst:
    m -= item
    if m < 0:
        break
    cnt += 1
print(cnt)
