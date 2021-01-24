n = int(input())
nums = list(map(int, input().split()))

avg = round(sum(nums) / n)
idx = 0
min_val = 1000
print(avg)
for i, v in enumerate(nums, start=1):
    if abs(v - avg) < abs(min_val - avg):
        idx = i
        min_val = v
    elif abs(v - avg) == abs(min_val - avg) and v > min_val:
        idx = i
        min_val = v
print(avg, idx)
