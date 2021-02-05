import sys

res = []
for _ in range(int(input())):
    nums = list(map(int, sys.stdin.readline().split()))
    max_val = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                val = (nums[i] + nums[j] + nums[k]) % 10
                if val > max_val:
                    max_val = val
    res.append(max_val)
max_val = max(res)
idx = 0
for i, v in enumerate(res):
    if v == max_val:
        idx = i
print(idx + 1)
