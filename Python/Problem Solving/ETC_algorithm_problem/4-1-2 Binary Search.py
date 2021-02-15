n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = 0
e = len(nums) - 1
while s <= e:
    mid = (s + e) // 2
    if nums[mid] > m:
        e = mid - 1
    elif nums[mid] < m:
        s = mid + 1
    else:
        break
print(mid + 1)
