n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
s, e = 0, 1
hap = lst[s]
while True:
    if hap < m:
        if e < n:
            hap += lst[e]
            e += 1
        else:
            break
    else:
        if hap == m:
            cnt += 1
        hap -= lst[s]
        s += 1

print(cnt)
