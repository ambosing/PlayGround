n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
hap = 0
s = 0
e = 0
while s < n:
    if hap < m and e < n:
        hap += a[e]
        e += 1
    else:
        if hap == m:
            cnt += 1
        hap -= a[s]
        s += 1
print(cnt)
