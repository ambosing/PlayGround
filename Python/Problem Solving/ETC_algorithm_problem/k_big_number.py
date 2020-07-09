n, t = map(int, input().split())
nums = list(map(int, input().split()))
lst = list()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            lst.append(nums[i] + nums[j] + nums[k])
lst = list(set(lst))
lst.sort(reverse=True)
print(lst[t - 1])
