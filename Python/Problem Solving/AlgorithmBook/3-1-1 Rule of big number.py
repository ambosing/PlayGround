n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

nums.sort()
i = 0
while i < m:
    for _ in range(k):
        res += nums[-1]
        i += 1
        if i == m:
            break
    else:
        res += nums[-2]
        i += 1
print(res)
