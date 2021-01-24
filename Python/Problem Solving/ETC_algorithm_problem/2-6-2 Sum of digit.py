def digit_sum(x):
    num = 0
    while x > 0:
        num += x % 10
        x //= 10
    return num


n = int(input())
nums = map(int, input().split())
max_val = 0
res = 0
for i in nums:
    val = digit_sum(i)
    if val > max_val:
        max_val = val
        res = i
print(res)
