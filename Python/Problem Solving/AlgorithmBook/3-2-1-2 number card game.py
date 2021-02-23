n, m = map(int, input().split())
max_val = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    val = min(nums)
    max_val = max(max_val, val)
print(max_val)
