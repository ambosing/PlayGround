n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] != nums[j]:
            cnt += 1
print(cnt)
