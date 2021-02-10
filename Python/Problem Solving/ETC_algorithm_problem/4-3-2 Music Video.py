def grouping(a):
    cnt = 1
    num = 0
    for item in lst:
        num += item
        if num > a:
            cnt += 1
            num = item
    return cnt


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = 0
e = sum(lst)
res = 0
while s <= e:
    mid = (s + e) // 2
    c = grouping(mid)
    if mid >= lst[-1] and c <= m:
        e = mid - 1
        res = mid
    else:
        s = mid + 1
print(res)
