def next_permutation(nums):
    len_n = len(nums) - 1
    i = len_n
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:
        return False
    j = len_n
    while nums[i - 1] >= nums[j]:
        j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    j = len_n
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return True


n = int(input())
lst = list(map(int, input().split()))
if next_permutation(lst):
    lst = list(map(str, lst))
    print(' '.join(lst))
else:
    print(-1)
