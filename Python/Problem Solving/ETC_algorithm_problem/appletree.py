n = int(input())
limit = (n + 1) // 2 # 3
res = 0

s = limit - 1
e = limit
for i in range(n):
    nums = list(map(int, input().split()))
    if i < limit:
        s_idx = s - i
        e_idx = e + i
    else:
        s_idx += 1
        e_idx -= 1
    res += sum(nums[s_idx:e_idx])
print(res)
