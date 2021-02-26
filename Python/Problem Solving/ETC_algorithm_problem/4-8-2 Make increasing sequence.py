n = int(input())
nums = list(map(int, input().split()))
lst = []
lt = 0
rt = n - 1
while lt <= rt:
    if nums[lt] > nums[rt]:
        if not lst or lst[-1][0] < nums[rt]:
            lst.append((nums[rt], 'R'))
            rt -= 1
            continue
    else:
        if not lst or lst[-1][0] < nums[lt]:
            lst.append((nums[lt], 'L'))
            lt += 1
            continue
    if lst[-1][0] < nums[lt]:
        lst.append((nums[lt], 'L'))
        lt += 1
    elif lst[-1][0] < nums[rt]:
        lst.append((nums[rt], 'R'))
        rt -= 1
    else:
        break

print(len(lst))
for i, v in enumerate(lst):
    print(v[1], end="")
