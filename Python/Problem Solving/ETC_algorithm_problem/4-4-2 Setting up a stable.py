def return_dis(m):
    max_dis = 0
    cnt = 1
    pre = lst[0]
    for i in lst:
        val = pre - i
        if val > m:
            if max_dis < val:
                max_dis = val
            pre = i
            cnt += 1
    return max_dis, cnt


n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
s = 1
e = lst[-1]
res = 0
while s <= e:
    mid = (s + e) // 2
    print(mid)
    dis, cnt = return_dis(mid)
    if cnt < c:
        e = mid - 1
    else:
        s = mid + 1
        res = dis
print(res)
