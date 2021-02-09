def cut_lan(a):
    cnt = 0
    for i, v in enumerate(lan):
        cnt += v // a
    return cnt


k, n = map(int, input().split())
lan = list()
for _ in range(k):
    lan.append(int(input()))
s = 0
e = max(lan)
res = 0
while s <= e:
    mid = (s + e) // 2
    c = cut_lan(mid)
    if c >= n:
        s = mid + 1
        res = mid
    else:
        e = mid - 1
print(res)
