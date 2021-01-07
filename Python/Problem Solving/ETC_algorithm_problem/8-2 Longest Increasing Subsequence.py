n = int(input())
nums = list(map(int, input().split()))
lst = [0] * n
lst[0] = 1

for i in range(1, n):
    idx = i
    for j in range(i - 1, -1, -1):
        if nums[j] < nums[i] and lst[idx] < lst[j]:
            idx = j
    if idx != 0:
        lst[i] = lst[idx] + 1
    else:
        lst[i] = 1
print(lst)
print(max(lst))
