n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
s = 0
e = n - 1

cnt = 0
while s <= e:
    all_w = w[s] + w[e]
    if all_w > m:
        e -= 1
        cnt += 1
    else:
        s += 1
        e -= 1
        cnt += 1
print(cnt)
