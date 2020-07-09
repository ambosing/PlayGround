def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res


n = int(input())
lst = list(map(int, input().split()))
max_val = -1
result = 0
for i, v in enumerate(lst):
    temp = digit_sum(v)
    if max_val < temp:
        max_val = temp
        result = v
print(result)
