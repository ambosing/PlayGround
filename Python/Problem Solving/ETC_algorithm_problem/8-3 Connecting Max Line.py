n = int(input())
nums = list(map(int, input().split()))

lst = [0] * n
lst[0] = 1

for i in range(1, n):
    max_val = 0
    for j in range(i - 1, -1, -1):
        if nums[j] < nums[i] and max_val < lst[j]:
            max_val = lst[j]
    lst[i] = max_val + 1

print(max(lst))
