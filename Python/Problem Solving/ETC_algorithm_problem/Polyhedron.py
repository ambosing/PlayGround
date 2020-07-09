n, m = map(int, input().split())
nums = [0] * (n + m + 1)
res = list()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        nums[i + j] += 1

max_val = max(nums)
for i, v in enumerate(nums):
    if max_val == v:
        res.append(str(i))
print(' '.join(res))
