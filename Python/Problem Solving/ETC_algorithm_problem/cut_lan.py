import sys


def count_lan(nums, x):
    cnt = 0
    for item in nums:
        cnt += item // x
    return cnt


k, n = map(int, input().split())
lst = list()

for _ in range(k):
    lst.append(int(sys.stdin.readline().rstrip()))

l_idx = 1
r_idx = max(lst)
res = 0
while l_idx <= r_idx:
    mid = (l_idx + r_idx) // 2
    if count_lan(lst, mid) >= n:
        l_idx = mid + 1
        res = mid
    else:
        r_idx = mid - 1
print(res)
