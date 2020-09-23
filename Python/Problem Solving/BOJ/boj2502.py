def solution():
    d, k = map(int, input().split())
    i = 1
    ii = i + 1
    while True:
        cnt = 2
        a = [i, ii]
        while cnt < d and a[-1] < k:
            a.append(a[cnt - 1] + a[cnt - 2])
            cnt += 1
        if cnt == d and a[-1] == k:
            print(i, ii, sep="\n")
            break
        if cnt == d:
            ii += 1
        elif a[-1] >= k:
            i += 1
            ii = i + 1


solution()
