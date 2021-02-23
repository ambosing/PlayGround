res = 0
nums = list(map(int, input()))
for num in nums:
    if res == 0:
        res = num
    elif num <= 1:
        res += num
    else:
        res *= num
print(res)

