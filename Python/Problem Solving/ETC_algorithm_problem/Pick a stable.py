def count(lst, len_lst, m):
    cnt = 1
    pre = lst[0]
    for i in range(1, len_lst):
        if lst[i] - pre >= m:
            cnt += 1
            pre = lst[i]
    return cnt


n, c = map(int, input().split())
dist = list()
for _ in range(n):
    dist.append(int(input()))
dist.sort()
lt = 1
rt = max(dist) - min(dist)
while lt <= rt:
    mid = lt + (rt - lt) // 2
    if count(dist, n, mid) >= c:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1
print(res)

