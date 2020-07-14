def check(nums, limit):
    hap = 0
    cnt = 1
    for i in nums:
        hap += i
        if hap > limit:
            cnt += 1
            hap = i
    return cnt


n, m = map(int, input().split())
lst = list(map(int, input().split()))
max_val = max(lst)
lt = 1
rt = sum(lst)
res = 0

while lt <= rt:
    mid = lt + (rt - lt) // 2
    if mid >= max_val and check(lst, mid) <= m:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1
print(res)

