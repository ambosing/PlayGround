from sys import maxsize


def rem_height(a):
    num = 0
    for i in h:
        if i > a:
            num += i - a
    return num


n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
lt = 0
rt = h[-1]
hap = rt
pre = maxsize
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    height = rem_height(mid)
    if height < m:
        rt = mid - 1
    elif height > m:
        lt = mid + 1
    else:
        break
print(mid)
