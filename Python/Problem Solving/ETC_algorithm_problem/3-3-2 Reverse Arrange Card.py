nums = [str(i) for i in range(1, 21)]

for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    for i in range((e - s + 1) // 2):
        nums[s + i], nums[e - i] = nums[e - i], nums[s + i]
print(' '.join(nums))
