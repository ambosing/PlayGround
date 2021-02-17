def distance_cnt(m):
    cnt = 1
    min_dis = int(1e9)
    pre = nums[0]
    for i in range(1, len(nums)):
        dis = nums[i] - pre
        if dis >= m:
            cnt += 1
            if min_dis > dis:
                min_dis = dis
            pre = nums[i]
    return min_dis, cnt


n, c = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
s = 1
e = nums[-1]
res = 0
while s <= e:
    mid = (s + e) // 2
    distance, count = distance_cnt(mid)
    if count < c:
        e = mid - 1
    else:
        s = mid + 1
        if res < distance:
            res = distance
print(res)
